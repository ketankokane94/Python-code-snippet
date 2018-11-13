from btnode import BTNode


class BST:

    __slots__ = 'root', 'size','index'

    def __init__(self):
        self.root = None
        self.size = 0
        self.index = 0

    def __insert(self, val, node):
        if val < node.val:
            if node.left is None:
                node.left = BTNode(val,index=self.index)
                self.index += 1
            else:
                self.__insert(val, node.left)
        else:
            if node.right is None:
                node.right = BTNode(val,index=self.index)
                self.index += 1
            else:
                self.__insert(val, node.right)

    def insert(self, val):
        if self.root is None:
            self.root = BTNode(val,index=self.index)
            self.index += 1
        else:
            self.__insert(val, self.root)
        self.size += 1

    def __inorder(self, node):
        if node is None:
            return ' '
        else:
            return self.__inorder(node.left) + \
                   str(node.val) + \
                   self.__inorder(node.right)


    def __based_on_value(self, node, acc = '', number_of_elements_printed =
    0):
        '''
        added an acc and index param to check how many number are printed as
        of now to get proper output
        :param node:
        :param acc:
        :param number_of_elements_printed:
        :return:
        '''
        if number_of_elements_printed > 2 or node is None:
            acc += ' '
            return acc, number_of_elements_printed

        else:
            acc,number_of_elements_printed = self.__based_on_value(node.left,acc,
                                         number_of_elements_printed)
            if number_of_elements_printed < 3:
                acc += str(node.val)
            number_of_elements_printed +=1
            acc, number_of_elements_printed = self.__based_on_value(node.right,
                                                                    acc,
                                                                    number_of_elements_printed)
            return acc,number_of_elements_printed


    def __inorder_using_index(self,node,index_to_look_for):
        if node is None:
            return
        else:
            self.__inorder_using_index(node.left,index_to_look_for)
            if node.index == index_to_look_for:
                print(node.val,end=' ')
            self.__inorder_using_index(node.right,index_to_look_for)




    def __str__(self):
        return self.__inorder(self.root)

    def first_three_added_order(self):
        for _ in range(3):
            self.__inorder_using_index(self.root,_)
        return ''

    def first_three_value_order(self):
        return self.__based_on_value(self.root)[0]


def test():
    tree = BST()
    to_add = [5,3,6,2,7,1]
    for _ in to_add:
        tree.insert(_)
    print(tree)
    print('first three value order:',end='  ')
    print(tree.first_three_added_order())
    print('first three value order:',tree.first_three_value_order())


if __name__ == '__main__':
    test()