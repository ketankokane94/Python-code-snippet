class BTNode:

    __slots__ = 'val', 'left', 'right','index'

    def __init__(self, val, index,left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.index = index
