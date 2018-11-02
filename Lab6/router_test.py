from stack import  Stack
from Queue import  Queue

# as ListQueue and ListStacks file could not uploaded added them in router
# Test python file only

## IMPORTANT, in Bryan's implementation of ListStack size is not handled
# properly

class ListQueue:
    '''
    This is a list based implementation of a queue which will keep oldest data
    and drop anything new that there is not room for
    '''
    def __init__(self, capacity):
        # create list of size capacity
        self.list_queue = [None] * capacity
        # store as instance variable
        self._capacity = capacity
        # set other instance variable defaults
        self.front = -1
        self.back = -1
        self.size = 0

    def __str__(self):
        # pretty print
        result = 'ListQueue['
        for val in self.list_queue:
            result += ' ' + str(val)
        return result + ']'

    def insert(self, val):
        # if at end of list, ignore add
        if self.back is self._capacity - 1:
            return
        # update pointers during insert to keeping only oldest data
        if self.front is -1:
            self.front = 0
        self.back += 1
        self.list_queue[self.back] = val
        self.size += 1

    def remove(self):
        # no op if empty
        if self.size is 0:
            return
        # update pointers
        self.list_queue = self.list_queue[1:] + [None]
        self.back -= 1
        if self.back is -1:
            self.front = -1
        self.size -= 1

    def peek(self):
        return self.list_queue[self.front]

    def capacity(self):
        return self._capacity


def test():
    print('Creating empty ListQueue named "a" of size 3')
    a = ListQueue(3)
    print('Creating empty ListQueue named "b" of size 2')
    b = ListQueue(2)

    print('peek on a', a.peek(), 'currently contains', a)
    print('peek on b', a.peek(), 'currently contains', b)
    for val in range(3):
        print('inserting', val, 'into both a and b')
        a.insert(val)
        # won't fit all
        b.insert(val)
        print('peek on a', a.peek(), 'currently contains', a)
        print('peek on b', a.peek(), 'currently contains', b)

    for i in range(2):
        print('removing', a.peek(), 'from a')
        a.remove()
        print('peek on a', a.peek(), 'currently contains', a)
        print('removing', b.peek(), 'from b')
        b.remove()
        print('peek on b', a.peek(), 'currently contains', b)

    for val in range(2):
        print('inserting', val, 'into both a and b')
        a.insert(val)
        b.insert(val)
        print('peek on a', a.peek(), 'currently contains', a)
        print('peek on b', a.peek(), 'currently contains', b)


class ListStack:
    '''
    This is a list based implementation of a stack which will keep newest data
    and drop anything oldest that there is not room for
    '''
    def __init__(self, capacity):
        # create list of size capacity
        self.list_stack = [None] * capacity
        # store as instance variable
        self._capacity = capacity
        # set other instance variable defaults
        self.top = -1
        self.size = 0

    def __str__(self):
        # pretty print
        result = 'ListStack['
        for val in self.list_stack[self.top::-1]:
            result += ' ' + str(val)
        for val in self.list_stack[-1:self.top:-1]:
            result += ' ' + str(val)
        return result + ']'

    def insert(self, val):
        # update pointers during insert to keep only newest data
        self.top += 1
        if self.top == self._capacity:
            self.top = 0
        self.list_stack[self.top] = val
        self.size += 1

    def remove(self):
        # no op if empty
        if self.size is 0:
            return
        # update pointers
        self.list_stack[self.top] = None
        self.top -= 1
        if self.top is -1:
            self.top = self._capacity - 1

    def peek(self):
        return self.list_stack[self.top]

    def capacity(self):
        return self._capacity

def test():
    print('Creating empty ListStack named "a" of size 3')
    a = ListStack(3)
    print('Creating empty ListStack named "b" of size 2')
    b = ListStack(2)

    print('peek on a', a.peek(), 'currently contains', a)
    print('peek on b', a.peek(), 'currently contains', b)
    for val in range(3):
        print('inserting', val, 'into both a and b')
        a.insert(val)
        # won't fit all
        b.insert(val)
        print('peek on a', a.peek(), 'currently contains', a)
        print('peek on b', a.peek(), 'currently contains', b)

    for i in range(2):
        print('removing', a.peek(), 'from a')
        a.remove()
        print('peek on a', a.peek(), 'currently contains', a)
        print('removing', b.peek(), 'from b')
        b.remove()
        print('peek on b', a.peek(), 'currently contains', b)

    for val in range(2):
        print('inserting', val, 'into both a and b')
        a.insert(val)
        b.insert(val)
        print('peek on a', a.peek(), 'currently contains', a)
        print('peek on b', a.peek(), 'currently contains', b)


from ListQueue import  ListQueue


def test_insert_of_stacks():
    print("=============testing insert into stacks==================")
    for _ in range(15):
        my_stack.push(_)
        listStack.insert(_)

    print('my_stack.size()',my_stack.size())
    print('sir_stack.size()', listStack.size)

    print('my_stack',my_stack)
    print('listStack',listStack)


def test_insert_into_queues():
    print("=============testing insert into queue==================")
    for _ in range(15):
        my_queue.enqueue(_)
        listQueue.insert(_)

    print('my_queue.size()',my_queue.size())
    print('listQueue.size()', listQueue.size)

    print('my_queue',my_queue)
    print('listQueue',listQueue)


"""
Helper function which creates two Queues
"""
def create_two_queues():
    return Queue(10), ListQueue(10)


"""
Helper function which creates two stacks
"""
def create_two_stacks():
    return Stack(10), ListStack(10)


"""
calls pop and peeks on two stacks to check if the elements are returned in 
same order
"""
def test_pop_of_stacks():
    error_flag = False
    print("=============testing pop into two stacks ==================")
    for _ in range(my_stack.size()):
        if my_stack.pop() is not listStack.peek():
            print('ERROR!!! the elements in two stack does not match')
            error_flag = True
            break
        listStack.remove()
    if not error_flag:
        print('elements in both the stack matched with order')


def test_remove_dequeue_of_queues():
    error_flag = False
    print("=============testing removes from two queue ==================")
    for _ in range(my_queue.size()):
        if my_queue.dequeue() is not listQueue.peek():
            print('ERROR!!! the elements in two queue does not match')
            error_flag = True
            break
        listQueue.remove()
    if not error_flag:
        print('elements in both the queue matched with order')


"""
main driver function of the router test 
"""
if __name__ == '__main__':
    my_stack, listStack = create_two_stacks()
    test_insert_of_stacks()
    test_pop_of_stacks()
    my_queue, listQueue = create_two_queues()
    test_insert_into_queues()
    test_remove_dequeue_of_queues()
