__author__ = 'kk'
from collections import namedtuple
import re

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''

class _delobj:
    pass


DELETED = Entry(_delobj(),None)


def hash_function2(key):
    '''
    Not using Python's built in hash function here since we want to
    have repeatable testing...
    However it is terrible.
    Assumes keys have a len() though...
    :param key: Key to store
    :return: Hash value for that key
    '''
    # if we want to switch to Python's hash function, uncomment this:
    # return hash(key)
    return len(key)


def hash_function1(string):
    prime_numbers = [179,127,233,283,103]
    sum = 0
    _ = 0
    for char in string:
        ordinal_value = ord(char)
        ordinal_value *= prime_numbers[ordinal_value % 5]
        sum += ordinal_value
    return sum


class Hashmap:

    __slots__ = 'table','numkeys', 'capacity', 'maxload','hashfunction', \
                'probe_count','collision_count'

    def __init__(self, hashfunction = None, initial_size=100,
                 maxload=0.7):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initial_size: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.collision_count = 0
        if hashfunction is None:
            # use in built
            hashfunction = hash
        self.hashfunction = hashfunction
        self.probe_count = 0
        self.capacity = initial_size
        self.table = [None for _ in range(self.capacity)]
        self.numkeys = 0
        self.maxload = maxload

    def put(self,key, value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        index = self.hashfunction(key) % self.capacity
        start = index
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key,value)

        if start != index:
            self.collision_count += 1

        self._increment_probe_count(start, index)

        if self.numkeys/self.capacity > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.capacity *= 2
            self.table = [None for _ in range(self.capacity)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None and entry != DELETED:
                    self.put(entry.key,entry.value)




    def remove(self,key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hashfunction(key) % self.capacity
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED


    def get(self,key):
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hashfunction(key) % self.capacity
        start = index
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.capacity:
                index = 0
        if self.table[index] is not None:
            self._increment_probe_count(start,index)
            return self.table[index].value
        else:
            raise KeyError('Key ' + str(key) + ' not present')

    def contains(self,key):
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''

        index = self.hashfunction(key) % self.capacity
        start = index
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == self.capacity:
                index = 0
        self._increment_probe_count(start,index)
        return self.table[index] is not None



    def _increment_probe_count(self, start, index):
        if start > index:
            # means wrapping up happened
            self.probe_count += self.capacity - start
            start = 0
        self.probe_count += index - start + 1


def printMap(map):
    for i in range(map.capacity):
        print(str(i)+": " + str(map.table[i]))

def testMap():
    #map = Hashmap(hash_func, initial_size=5)
    map = Hashmap(hash_function1, initial_size=500)
    map.put('apple',1)
    map.put('banana',2)
    map.put('orange',15)
    printMap(map)
    print('probes = ', map.probe_count)
    print('collision = ', map.collision_count)


    print(map.contains('apple'))
    print(map.contains('grape'))
    print(map.get('orange'))



    print('--------- adding one more to force table resize ')
    map.put('grape',7)
    printMap(map)

    print('--------- testing remove')
    map.remove('apple')
    printMap(map)

    print('--------- testing add to a DELETED location')
    map.put('peach',16)
    printMap(map)
    print(map.get('grape'))


def read_words_from_dict():
    words = []
    with open('/usr/share/dict/words') as file:
        for lines in file:
            if lines is not '' and len(words) <= 50000:
                words.extend(re.split('\W+',lines.strip().lower()))
    return words


def test_map_with_hash_function_and_load_factor(hash_functin_name,
                                                hash_function,
                                                load_factor,
                                                words):
    map = Hashmap(hash_function, initial_size=30000,maxload=load_factor)
    for _ in range(len(words)):
        try:
            word = words[_]
            value = map.get(word)
            map.put(word, value + 1)
        except:
            map.put(word, 1)
    print('================== Results for ========================')
    print('result with ',hash_functin_name, ' with load factor ',\
    load_factor)
    print('probes = ', map.probe_count)
    print('collision = ', map.collision_count)


def main():
    words = read_words_from_dict()
    test_map_with_hash_function_and_load_factor('internal hash function',None,
                                                0.7, words)
    test_map_with_hash_function_and_load_factor('internal hash function',
                                                None, 0.8, words)
    test_map_with_hash_function_and_load_factor('internal hash function',
                                                None, 0.9, words)
    test_map_with_hash_function_and_load_factor('hash function1',
                                                hash_function1,0.7,words)
    test_map_with_hash_function_and_load_factor('hash function1',
                                                hash_function1, 0.8, words)
    test_map_with_hash_function_and_load_factor('hash function1',
                                                hash_function1, 0.9, words)


if __name__ == '__main__':
    main()
# TODO, make a new hash function, send the file thru the novels and
# TODO  : dictionary and tabulate the result and upload the code




'''
Send each of these through your main method, testing your two hash functions as well
 as Python’s builtin hash function over three different maximum load factors of your choice.
Then, you should collect and report on the data that you have obtained. Compare the results 
from the different input files, hash functions and load factors in tabular
 and/or graphical form, putting this in a PDF document.

'''

