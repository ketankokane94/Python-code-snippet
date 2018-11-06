__author__ = 'kk'
'''
this script uses different hash functions to see how they affect the 
performance of the hash map. also measure the effect of load factor on the 
hash map.

for benchmarking, the script uses hashmap to store one dictionary with 50000 
words in it. and does operations on it using different hash functions.
'''
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


def hash_function2(string):
    '''
    this hash function uses bit operation to generate a number based on the
    string passed.

    algo used :
    iterate over the string, for every character in the string
    find its ordinal value, left shift it by 3
    then to keep it bounded and make the posistion of the char in the string
    imp take it mod with one of the 5 prime numbers
    on every character take the mod of the calculated hash to keep it bounded
    :param string:
    :return:
    '''
    prime_numbers = [179, 127, 233, 283, 103]
    hash = 1
    _ = 0
    for char in string:
        # take ordinal value and bit shift by 3
        int_value = ord(char) << 3
        # mod it with one of the 5 prime number to keep it bounded
        int_value = int_value % prime_numbers[ord(char) % 5]
        if _ % 2 is 0:
            # to keep the total hash value bounded mod it with a bigger prime
            #  number
            hash = hash % 102233
        _ += 1
        # keep building the hash value
        hash *= int_value
    return hash


def hash_function1(string):
    '''

    :param string:
    :return:
    '''
    # list of random prime numbers used to keep the hash bounded
    prime_numbers = [179,127,233,283,103]
    # we use summation to build up the final hash, so iniialise it to 0
    sum = 0

    for char in string:
        # for every character in the string calculate the ordinal value
        ordinal_value = ord(char)
        # multiply the ordinal value with one of the prime number this is
        # basically to pump up the values
        ordinal_value *= prime_numbers[ordinal_value % 5]
        # build up the final hash
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

        # if the index (hash) given by the hash function has been chaneged,
        # then it implies that a collision occurred.

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
        '''
        start is the hash code retured by the hash function,
        based on the size of the hash map calculate the how far the index
        moved from the original generated hash value, the distance cane be
        thought of as the probe.
        :param start:
        :param index:
        :return:
        '''

        if start > index:
            # means wrapping up happened
            self.probe_count += self.capacity - start
            # reset it to start
            start = 0
        # how far off is the index from start, that many probes where made
        self.probe_count += index - start + 1


def printMap(map):
    for i in range(map.capacity):
        print(str(i)+": " + str(map.table[i]))


def read_words_from_dict():
    '''
    creates a word list from either the dictionary or the alice in wonderland book
    :return:
    '''
    words = []
    #with open('alice.txt') as file:
    with open('/usr/share/dict/words') as file:
        for lines in file:
            # when the number of words increases the performance is really
            # slowed down, so keeping the max limit to 50000
            if lines is not '' and len(words) <= 50000:
                words.extend(re.split('\W+',lines.strip().lower()))
    return words


def test_map_with_hash_function_and_load_factor(hash_functin_name,
                                                hash_function,
                                                load_factor,
                                                words):
    '''
    helper function which runs the hash map experiment with different hash
    functions and different load factor
    :param hash_functin_name:
    :param hash_function:
    :param load_factor:
    :param words:
    :return:
    '''
    map = Hashmap(hash_function, initial_size=5000,maxload=load_factor)
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
    test_map_with_hash_function_and_load_factor('hash function2',
                                                hash_function2, 0.7, words)
    test_map_with_hash_function_and_load_factor('hash function2',
                                                hash_function2, 0.8, words)
    test_map_with_hash_function_and_load_factor('hash function2',
                                                hash_function2, 0.9, words)


if __name__ == '__main__':
    main()

# TODO  : dictionary and tabulate the result and upload the code




'''
Send each of these through your main method, testing your two hash functions as well
 as Python’s builtin hash function over three different maximum load factors of your choice.
Then, you should collect and report on the data that you have obtained. Compare the results 
from the different input files, hash functions and load factors in tabular
 and/or graphical form, putting this in a PDF document.

'''

