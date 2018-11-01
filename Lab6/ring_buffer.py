'''
have to create 4 files
ringbuffer
stack
queue
test_router

each class should have its own test function

• insert keep new - Add item at next location, keeping new data
• insert keep old - Add item at next location, keeping old data
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


    def replace(self,cursor, new_value):
        # should return a true or false value
        if cursor is not None:
            if self._the_cursor_exists_in_the_list(cursor):
                cursor.value = new_value
                return True
        else:
            # cursor was None
            return False


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

    def is_buffer_full(self):
        return self.size() is self.capacity()

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

    def _remove_the_only_node(self):
        returnValue = self._tail.value
        self._tail = None
        self._number_of_nodes = 0
        return returnValue

    def remove_newest(self):
        # in ring buffer we append element to the tail so remove newest means
        # remove the last added element
        returnValue = None
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
        returnValue = self._tail.value
        cursor.next = self._tail.next
        self._tail = cursor
        return returnValue

    def remove_oldest(self):
        # in ring buffer we append element to the tail so remove oldest means
        # remove the first added element
        returnValue = None
        if self._number_of_nodes is 0:
            return None

        if self._number_of_nodes is 1:
            return self._remove_the_only_node()

        head = self._tail.next
        self._number_of_nodes -= 1

        # now the cursor is the pointing to the first node
        returnValue = head.value
        self._tail.next = head.next
        return returnValue

    # used by queue
    def insert_keep_old(self,value):
        if self.is_buffer_full():
            pass
        else:
            self._add(value)

    # to be used by stack
    def insert_keep_new(self,value):
        if self.is_buffer_full():
            self.remove_newest()
            self._add(value)
        else:
            self._add(value)


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

    # testing find functionality
    # 1 element which is present
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

    #print(ring_buffer._the_cursor_exists_in_the_list(ring_buffer.find(1)))
    #print(ring_buffer._the_cursor_exists_in_the_list(ring_buffer.find(9)))
    # replace
    # 1. pass existing cursor to replace function and see if value is updated
    print(ring_buffer.replace(ring_buffer.find(1),0))
    print(ring_buffer)
    # 2. pass None cursor should not update anything
    print(ring_buffer.replace(ring_buffer.find(9),0))
    print(ring_buffer)
    # 3. the structure of the node should not be changed
    print(ring_buffer.replace(ring_buffer.find(4), 0))
    print(ring_buffer)
    print(ring_buffer.replace(ring_buffer.find(0), 1))
    print(ring_buffer)

    # remove remove_newest
    print('size of ring buffer before remove',ring_buffer._number_of_nodes)
    print(ring_buffer)
    print('removed element:',ring_buffer.remove_newest())
    print(ring_buffer)
    print('size of ring buffer after remove', ring_buffer._number_of_nodes)

    #remove when ringBUffer is empty returns None
    print('remove when ringBUffer is empty should return None :',RingBuffer(

    ).remove_newest())

    #removes newest when only one element is contained in the list should
    # empty the list
    rb = RingBuffer()
    rb._add(1)
    rb.remove_newest()
    print(rb)

    # remove oldest

    print('remove oldest')
    print(ring_buffer)
    print('remove oldest',ring_buffer.remove_oldest())
    print(ring_buffer)
    print('remove oldest', ring_buffer.remove_oldest())
    print(ring_buffer)
    print('remove oldest', ring_buffer.remove_oldest())
    print(ring_buffer)


if __name__ == '__main__':
    test()
