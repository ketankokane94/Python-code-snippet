from ring_buffer import RingBuffer

class Queue:


    __slots__ = 'ring_buffer','max_capacity'

    def __init__(self,capacity = 10):
        self.ring_buffer = RingBuffer(capacity)
        self.max_capacity = capacity

    def __str__(self):
        return str(self.ring_buffer)

    def enqueue(self,value):
        if value is None:
            raise Exception('cannot enqueue None element in the queue')
        else:
            self.ring_buffer.insert_keep_old(value)

def test():
    my_queue = Queue(2)
    print('create a new queue and print empty queue :',my_queue)
    my_queue.enqueue(3)
    my_queue.enqueue(2)
    print('stack after pushing 3 and 2:', my_queue, '<-- end')
    print('my_stack.max_capacity = ', my_queue.max_capacity)
    my_queue.enqueue(1)
    print('enqueuing 1 after max size is reached should simply drop 1 :',
          my_queue, '<-- end')

if __name__ == '__main__':
    test()

