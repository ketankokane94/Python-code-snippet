__author__ = 'KK'

"""
CSCI-603 : intrumentation_sort.py Lab-6
Author : Ketan Kokane
This file provides the implementation to a queue using ring buffer data 
structure
"""

from ring_buffer import RingBuffer


class Queue:

    __slots__ = 'ring_buffer','max_capacity'

    """constructor with intial max capacity of 10"""
    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    """to string function uses the internal to string of ring buffer but 
       points to the end"""
    def __str__(self):
        return str(self.ring_buffer) +  '<-- end '

    """ enqueue function which inserts values in the queue """
    def enqueue(self,value):
        if value is None:
            raise Exception('cannot enqueue None element in the queue')
        else:
            self.ring_buffer.insert_keep_old(value)

    """ dequeue function which removes values from the queue using FIFO 
    method
        raises an exception if dequeue is done on the empty queue"""
    def dequeue(self):
        if self.ring_buffer.size() is 0:
            raise Exception('dequeue from a empty queue is not allowed')
        else:
            return self.ring_buffer.remove_oldest()

    """ returns the current size of the stack"""
    def size(self):
        return self.ring_buffer.size()

    """ :return the max capacity of the stack """
    def capacity(self):
        return self.ring_buffer.capacity()

    """ only returns the value of the first element in the queue does not 
       removed the element from the queue
       """
    def peek(self):
        if self.size() < 1:
            raise Exception('peek into a empty queue is not allowed')
        else:
            return self.ring_buffer.start_element()

def test():
    my_queue = Queue(2)
    print('create a new queue and print empty queue :',my_queue)
    print('======================== enqueue elements on the queue  '
          '===============')
    my_queue.enqueue(3)
    my_queue.enqueue(2)
    print('queue after enqueuing 3 and 2:', my_queue)
    print('myqueue.max_capacity = ', my_queue.max_capacity)
    my_queue.enqueue(1)
    print('enqueuing 1 after max size is reached should simply drop 1 :',
          my_queue)
    # dequeue from an empty queue should throw an exception
    print('======================== dequeue elements on the queue  '
          '===============')
    try:
        print('dequeue from a queue stack thorw an exception')
        Queue().dequeue()
    except Exception:
        print('exception thrown and caught')

    print('dequeue from queue ', my_queue, end='   returns  ')
    print(my_queue.dequeue())
    print('queue after dequeue',my_queue)
    # peek from empty should throw an exception
    print('======================== peek elements on the queue  '
          '===============')
    try:
        print('peek into a empty queue throw an exception')
        Queue().peek()
    except Exception:
        print('exception thrown and caught')

    my_queue.enqueue(5)
    print('peek into Queue ', my_queue, end='   returns  ')
    print(my_queue.peek())
    print('queue after peek', my_queue)


if __name__ == '__main__':
    test()

