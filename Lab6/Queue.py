from ring_buffer import RingBuffer


class Queue:

    __slots__ = 'ring_buffer','max_capacity'

    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    def __str__(self):
        return str(self.ring_buffer) +  '<-- end '

    def enqueue(self,value):
        if value is None:
            raise Exception('cannot enqueue None element in the queue')
        else:
            self.ring_buffer.insert_keep_old(value)

    def dequeue(self):
        if self.ring_buffer.size() is 0:
            raise Exception('dequeue from a empty queue is not allowed')
        else:
            return self.ring_buffer.remove_oldest()

    def size(self):
        return self.ring_buffer.size()

    def capacity(self):
        return self.ring_buffer.capacity()

    def peek(self):
        if self.size() < 1:
            raise Exception('peek into a empty queue is not allowed')
        else:
            return self.ring_buffer.start_element()



def test():
    my_queue = Queue(2)
    print('create a new queue and print empty queue :',my_queue)
    my_queue.enqueue(3)
    my_queue.enqueue(2)
    print('stack after pushing 3 and 2:', my_queue)
    print('my_stack.max_capacity = ', my_queue.max_capacity)
    my_queue.enqueue(1)
    print('enqueuing 1 after max size is reached should simply drop 1 :',
          my_queue)
    # dequeue from an empty queue should throw an exception
    try:
        print('dequeue from a queue stack thorw an exception')
        Queue().dequeue()
    except Exception:
        print('exception thrown and caught')

    print('dequeue from queue ', my_queue, end='   returns  ')
    print(my_queue.dequeue())
    # peek from empty should throw an exception
    try:
        print('peek into a empty queue throw an exception')
        Queue().peek()
    except Exception:
        print('exception thrown and caught')

    my_queue.enqueue(5)
    print('peek into Queue ', my_queue, end='   returns  ')
    print(my_queue.peek())


if __name__ == '__main__':
    test()

