from ring_buffer import RingBuffer

class Stack:


    __slots__ = 'ring_buffer','max_capacity'

    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    def __str__(self):
        return str(self.ring_buffer)

    def push(self,value):
        if value is None:
            raise Exception('cannot push None element in the stack')
        else:
            self.ring_buffer.insert_keep_new(value)



def test():
    my_stack = Stack(2)
    print('create a new stack and print empty stack :',my_stack,'<-- top')
    my_stack.push(3)
    my_stack.push(2)
    print('stack after pushing 3 and 2:', my_stack,'<-- top')
    print('my_stack.max_capacity = ',my_stack.max_capacity)
    my_stack.push(1)
    print('pushing 1 after max size is reached should replace 2 with 1 :',
          my_stack,'<-- top')



if __name__ == '__main__':
    test()

