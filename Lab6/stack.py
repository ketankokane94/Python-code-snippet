__author__ = 'KK'

"""
CSCI-603 : intrumentation_sort.py Lab-6
Author : Ketan Kokane
This file provides the implementation to a stack using ring buffer data 
structure
"""

from ring_buffer import RingBuffer


class Stack:
    __slots__ = 'ring_buffer','max_capacity'

    """
    constructor with intial max capacity of 10"""
    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    """to string function uses the internal to string of ring buffer but 
    points to the top"""
    def __str__(self):
        return str(self.ring_buffer) + ' <-- top'

    """ push function which inserts values in the stack """
    def push(self,value):
        if value is None:
            raise Exception('cannot push None element in the stack')
        else:
            self.ring_buffer.insert_keep_new(value)

    """ pop function which removes values from the stack using LIFO method
    raises an exception if pop is done on the empty stack"""
    def pop(self):
        if self.ring_buffer.size() is 0:
            raise Exception('poping from a empty stack is not allowed')
        else:
            return self.ring_buffer.remove_newest()

    """ returns the current size of the stack"""
    def size(self):
        return self.ring_buffer.size()

    """ :return the max capacity of the stack """
    def capacity(self):
        return self.ring_buffer.capacity()

    """ only returns the value of the top most element on the stack does not 
    removed the element from the stack
    """
    def peek(self):
        if self.size() < 1:
            raise Exception('peek into a empty stack is not allowed')
        else:
            return self.ring_buffer.end_element()


def test():
    my_stack = Stack(2)
    print('created a new my_stack = Stack(2)')
    print('print empty stack :',my_stack)
    print('======================== push elements on the stack  '
          '===============')
    my_stack.push(3)
    my_stack.push(2)

    print('stack after pushing 3 and 2:', my_stack)
    print('my_stack.max_capacity = ',my_stack.max_capacity)
    my_stack.push(1)
    print('pushing 1 after max size is reached 3 should be removed and 1 '
          'added :',
          my_stack)
    print('======================== pop elements from stack  '
          '===============')
    # poping from an empty stack should throw an exception
    try:
        print('poping from a empty stack throw an exception')
        Stack().pop()
    except Exception:
        print('exception thrown and caught')

    print('poping from stack ',my_stack,end='   returns  ')
    print(my_stack.pop())

    # peek from empty should throw an exception
    print('======================== peek elements from stack  '
          '===============')
    try:
        print('peek into a empty stack throw an exception')
        Stack().peek()
    except Exception:
        print('exception thrown and caught')
    my_stack.push(5)
    print('peek into stack ', my_stack, end='   returns  ')
    print(my_stack.peek())




if __name__ == '__main__':
    test()

