'''
have to create 4 files
ringbuffer
stack
queue
test_router

each class should have its own test function


• __str__ - String representation of you RingBuffer
• insert keep new - Add item at next location, keeping new data
• insert keep old - Add item at next location, keeping old data
• remove oldest - Remove oldest item in RingBuffer
• remove newest - Remove newest item in RingBuffer

• find(value) - Find item if in the list, return a cursor
• replace(cursor, val) - Replace this location - a use case might be using this after calling find


'''

# implement the given functions and use this class to implemenet a stack and
# queue

from mynode import MyNode





class RingBuffer:

    # data points which are required for the implementation of the RingBuffer
    __slots__ =  '_number_of_nodes', '_max_size', '_tail'

    def __init__(self,max_size = 16):
        self._number_of_nodes = 0
        self._max_size = max_size
        self._tail = None

    def size(self):
        return self._number_of_nodes

    def capacity(self):
        return self._max_size

    def find(self,value):
        cursor = self._tail
        while cursor is not None and cursor.next is not None:
            if cursor.value is value:
                return cursor
            cursor = cursor.next

    def replace(self,cursor,new_value):
        if cursor is not None:
            if self.the_cursor_exists_in_the_list(cursor):
                cursor.value =new_value
            else:
                raise Exception('provided cursor is not present in the buffer')
        else:
            raise Exception('cursor cannot be None')

    def __str__(self):
        if self.size() is 0:
            return '[]'
        else:
            result = 'RingBuffer [ '
            curr = self._tail.next
            while curr.next is not self._tail.next:
                result += str(curr.value)+ ' '
                curr = curr.next
            result += str(curr.value) + ' '
        result += ']'
        return result

    def the_cursor_exists_in_the_list(cursor):
        pass

    def _add(self,value):
        # this function is only called by internal implementation and when
        # size is less than then capacity
        if self._tail is None:
            # means this is the first element
            self._tail = MyNode(value)
            self._tail.next = self._tail
            self._number_of_nodes +=1
        else:
            # create a new node
            newNode = MyNode(value)
            # store the next of the last node i.e. head as it will be
            # overridden by new node
            head = self._tail.next
            # add new Node to next of last node
            self._tail.next = newNode
            # make the tail now point to the last node
            self._tail = newNode
            # now make the last node again point to first node
            newNode.next = head






def test():
    # when a new RingBUffer is created it should have proper Initialisations
    size = 32
    ring_buffer = RingBuffer(size)
    assert ring_buffer._tail is None and ring_buffer._max_size is size and \
           ring_buffer._number_of_nodes is 0, "ring buffer initialisation " \
                                             "failed"
    # size function should return the number of node variables
    ring_buffer._number_of_nodes = 5

    assert ring_buffer.size() is 5, "size() did not return 5"

    assert ring_buffer.capacity() is 32, "capacity() did not required max " \
                                         "size capacity"

    # testing toStr function
    # when the ring buffer is empty is should return a []
    ring_buffer = RingBuffer()
    assert str(ring_buffer) is not '[]', "str() for empty buffer did not return []"


    ring_buffer._add(1)
    ring_buffer._add(2)
    ring_buffer._add(3)
    ring_buffer._add(4)
    print(ring_buffer)




if __name__ == '__main__':
    test()
