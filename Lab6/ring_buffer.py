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
• find(value) - Find item if in the list, return a cursor


• replace(cursor, val) - Replace this location - a use case might be using this after calling find
• remove oldest - Remove oldest item in RingBuffer
• remove newest - Remove newest item in RingBuffer

'''

# implement the given functions and use this class to implemenet a stack and
# queue

from mynode import MyNode





class RingBuffer:

    # data points which are required for the implementation of the RingBuffer
    __slots__ =  '_number_of_nodes', '_max_size', '_head'

    def __init__(self,max_size = 16):
        self._number_of_nodes = 0
        self._max_size = max_size
        self._head = None

    def size(self):
        return self._number_of_nodes

    def capacity(self):
        return self._max_size

    def find(self,value):
        cursor = self._head
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

    def the_cursor_exists_in_the_list(cursor):
        pass






def test():
    # when a new RingBUffer is created it should have proper Initialisations
    size = 32
    ring_buffer = RingBuffer(size)
    assert ring_buffer._head is None and ring_buffer._max_size is size and \
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




if __name__ == '__main__':
    test()
