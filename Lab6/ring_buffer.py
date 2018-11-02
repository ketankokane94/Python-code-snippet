__author__ = 'KK'

"""
CSCI-603 : intrumentation_sort.py Lab-6
Author : Ketan Kokane
This file provides the implementation to ring buffer data structure
"""


class MyNode:

    slots = 'value', 'next'

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class RingBuffer:

    # data points which are required for the implementation of the RingBuffer
    __slots__ = '_number_of_nodes', '_max_size', '_tail'
    '''
    constructor to initialise a ring buffer with default max size of 16 nodes
    '''
    def __init__(self,max_size = 16):
        self._number_of_nodes = 0
        self._max_size = max_size
        self._tail = None

    """
    returns the number of elements in the list at any given time
    """
    def size(self):
        return self._number_of_nodes

    """
    returns the maximum capacity of the ring buffer 
    """
    def capacity(self):
        return self._max_size

    """
    searches for a given value in the buffer
    returns a cursor pointing to such a node
    """
    def find(self,value):
        cursor = self._tail.next
        while cursor is not self._tail:
            if cursor.value is value:
                return cursor
            cursor = cursor.next
        # due to our condition the last node does not get searched
        if self._tail.value is value:
            return self._tail
        else:
            return None

    """
    updates the value of the passed cursor with the new value
    this function is supposed to be used in combination with find method
    """
    def replace(self,cursor, new_value):
        # should return a true or false value
        if cursor is not None:
            if self._the_cursor_exists_in_the_list(cursor):
                cursor.value = new_value
                return True
        else:
            # cursor was None
            return False

    """
    used to print a pretty version of the ring Buffer internal structure
    """
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

    """
    helper function used to find if the current instance of ring buffer is 
    exhausted or no
    """
    def is_buffer_full(self):
        return self.size() is self.capacity()

    """
    helper function used by the replace function to check if the passed 
    cursor exists in the ring buffer or not
    """
    def _the_cursor_exists_in_the_list(self,cursor):
        if self._number_of_nodes is 0:
            return False
        else:
            # start from the head
            if self._tail is cursor:
                return True
            # if not then look in the rest of the list
            curr = self._tail.next
            while curr is not self._tail:
                if cursor is curr:
                    return True
                curr = curr.next
            return False

    """
    helper function used to add a new Node to the end of the list 
    implementation of the ring buffer 
    """
    def _add(self,value):
        self._number_of_nodes += 1
        # this function is only called by internal implementation and when
        # size is less than then capacity
        if self._tail is None:
            # means this is the first element
            self._tail = MyNode(value)
            self._tail.next = self._tail

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

    """
    helper function which is used when only one node exists in the buffer and needs to be removed
    """
    def _remove_the_only_node(self):
        returnValue = self._tail.value
        self._tail = None
        self._number_of_nodes = 0
        return returnValue

    """
    removes the most recently added node from the buffer 
    """
    def remove_newest(self):
        # in ring buffer we append element to the tail so remove newest means
        # remove the last added element
        if self._number_of_nodes is 0:
            return None

        if self._number_of_nodes is 1:
            return self._remove_the_only_node()

        cursor = self._tail.next
        self._number_of_nodes -=1

        #iterate to the second last e
        while cursor.next is not self._tail:
             cursor = cursor.next

        # now the cursor is the pointing to the second last node
        return_value = self._tail.value
        cursor.next = self._tail.next
        self._tail = cursor
        return return_value

    """
    removes the element from the list which is oldest in the list 
    can be thought of as head of the list , as we always add value to the 
    tail of the list
    """
    def remove_oldest(self):
        # in ring buffer we append element to the tail so remove oldest means
        # remove the first added element
        if self._number_of_nodes is 0:
            return None

        if self._number_of_nodes is 1:
            return self._remove_the_only_node()

        head = self._tail.next
        self._number_of_nodes -= 1

        # now the cursor is the pointing to the first node
        return_value = head.value
        self._tail.next = head.next
        return return_value

    # used by queue
    def insert_keep_old(self,value):
        if self.is_buffer_full():
            pass
        else:
            self._add(value)

    # to be used by stack
    def insert_keep_new(self,value):
        if self.is_buffer_full():
            self.remove_oldest()
            self._add(value)
        else:
            self._add(value)

    """
    returns the value of the last element in the list 
    """
    def end_element(self):
        if self.size() > 0:
            return self._tail.value
        else:
            return None

    """
    returns the first element in the list 
    """
    def start_element(self):
        if self.size() > 0:
            return self._tail.next.value
        else:
            return None


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

    # when the ring buffer is empty is should return a []
    ring_buffer = RingBuffer()
    assert str(ring_buffer) is not '[]', "str() for empty buffer did not return []"

    ring_buffer._add(1)
    ring_buffer._add(2)
    ring_buffer._add(3)
    ring_buffer._add(4)
    print(ring_buffer)

    # testing find functionality
    # 1 element which is present
    print('=======================testing find=======================')
    print('element '+ str(3) +' present in RingBuffer [ 1 2 3 4 ] ',
          ring_buffer.find(3) )
    # 2 element which is present in the end and start
    print('element ' + str(1) + ' present in RingBuffer [ 1 2 3 4 ]',
          ring_buffer.find(1))
    print('element ' + str(4) + ' present in RingBuffer [ 1 2 3 4 ]',
          ring_buffer.find(4))
    # 3 element which is not present
    print('element ' + str(5) + ' present in RingBuffer [ 1 2 3 4 ]',
          ring_buffer.find(5))

    print('============testing _the_cursor_exists_in_the_list========')
    print(ring_buffer._the_cursor_exists_in_the_list(ring_buffer.find(1)))
    print(ring_buffer._the_cursor_exists_in_the_list(ring_buffer.find(9)))
    # replace

    print('=======================testing replace=======================')
    print('before replace',ring_buffer)
    # 1. pass existing cursor to replace function and see if value is updated
    print('replace 1 with 0',ring_buffer.replace(ring_buffer.find(1),0))
    print('after replace',ring_buffer)
    # 2. pass None cursor should not update anything
    print('before replace', ring_buffer)
    print('try to replace a non existing element with '
          'something ',ring_buffer.replace(ring_buffer.find(9),0))
    print('after replace', ring_buffer)
    print(ring_buffer)
    # 3. the structure of the node should not be changed
    print('some more replace of end and start node to check the structure of '
          'the node is not updated')
    print(ring_buffer.replace(ring_buffer.find(4), 0))
    print(ring_buffer.replace(ring_buffer.find(0), 1))
    print(ring_buffer)

    print('=======================testing remove_newest=======================')
    # remove remove_newest
    print('size of ring buffer before remove',ring_buffer.size())
    print(ring_buffer)
    print('remove_newest():',ring_buffer.remove_newest())
    print(ring_buffer)
    print('size of ring buffer after remove', ring_buffer.size())

    #remove when ringBUffer is empty returns None
    print('remove_newest when ringBuffer is empty should return None :',
          RingBuffer(

    ).remove_newest())

    #removes newest when only one element is contained in the list should
    # empty the list
    print('newest when only one element is contained in the list')
    rb = RingBuffer()
    rb._add(1)
    rb.remove_newest()
    print(rb)

    # remove oldest

    print('=======================testing remove_oldest=======================')
    print(ring_buffer)
    print('remove oldest',ring_buffer.remove_oldest())
    print(ring_buffer)
    print('remove oldest', ring_buffer.remove_oldest())
    print(ring_buffer)
    print('remove oldest', ring_buffer.remove_oldest())
    print(ring_buffer)
    print('=======================END=======================')



if __name__ == '__main__':
    test()
