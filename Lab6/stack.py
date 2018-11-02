from ring_buffer import RingBuffer

class Stack:


    __slots__ = 'ring_buffer','max_capacity'

    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    def __str__(self):
        return str(self.ring_buffer) + ' <-- top'

    def push(self,value):
        if value is None:
            raise Exception('cannot push None element in the stack')
        else:
            self.ring_buffer.insert_keep_new(value)

    def pop(self):
        if self.ring_buffer.size() is 0:
            raise Exception('poping from a empty stack is not allowed')
        else:
            return self.ring_buffer.remove_newest()

    def size(self):
        return self.ring_buffer.size()

    def capacity(self):
        return self.ring_buffer.capacity()

    def peek(self):
        if self.size() < 1:
            raise Exception('peek into a empty stack is not allowed')
        else:
            return  self.ring_buffer.end_element()



def test():
    my_stack = Stack(2)
    print('create a new stack and print empty stack :',my_stack)
    my_stack.push(3)
    my_stack.push(2)
    print('stack after pushing 3 and 2:', my_stack)
    print('my_stack.max_capacity = ',my_stack.max_capacity)
    my_stack.push(1)
    print('pushing 1 after max size is reached should replace 2 with 1 :',
          my_stack)

    # poping from an empty stack should throw an exception
    try:
        print('poping from a empty stack throw an exception')
        Stack().pop()
    except Exception:
        print('exception thrown and caught')

    print('poping from stack ',my_stack,end='   returns  ')
    print(my_stack.pop())

    # peek from empty should throw an exception
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

