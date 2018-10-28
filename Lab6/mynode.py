class MyNode:

    slots = 'value', 'next'

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


def test():
    node = MyNode(5)
    nextNode = MyNode(6)
    node.next = nextNode
    nextNode = node
    while nextNode is not None:
        print(nextNode)
        nextNode = nextNode.next


if __name__ == '__main__':
    test()

