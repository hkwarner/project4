import random

class Binary_Search_Tree:

    class __BST_Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.__root = None

    def rec_insert(self, value, cur_node): # should be correct
        if cur_node == None:
            return self.__BST_Node(value)
        elif cur_node != None:
            if value < cur_node.value:
                cur_node.left = self.rec_insert(value, cur_node.left)
            elif value > cur_node.value:
                cur_node.right = self.rec_insert(value, cur_node.right)
            elif value == cur_node.value:
                raise ValueError
            return cur_node

    def insert_element(self, value):
        self.__root = self.rec_insert(value, self.__root)

    def remove_element(self, value):
        if self.__root == None: print('root is None before removal')
        self.__root = self.__rec_remove(value, self.__root)
        if self.__root == None: print('root is None') #self.__root is being returned as none-->not assigned

    def __rec_remove(self, value, cur_node):
        if cur_node == None:
            raise ValueError
        if value < cur_node.value:
            cur_node.left = self.__rec_remove(value, cur_node.left)
        elif value > cur_node.value:
            cur_node.right = self.__rec_remove(value, cur_node.right)
        elif value == cur_node.value: # value found
            if cur_node.left != None and cur_node.right != None:
                prec = cur_node
                replace_with = cur.right
                while replace_with.left != None:
                    prec = replace_with
                    replace_with = replace_with.left
                current.val = replace_with.val #this should probably return something
                prec.left = None
            elif cur_node.right == None:
                cur_node = cur_node.left
            elif cur_node.left == None:
                cur_node = cur_node.right
        return cur_node

    def in_order(self):
        string = self.__rec_in_order(self.__root)
        string = string.split()
        to_return = ''
        for i in string:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_in_order(self, cur_node):
        to_return = ''
        if cur_node == None:
            return ''
        elif cur_node != None:
            tree = [self.__rec_in_order(cur_node.left), \
            str(cur_node.value), \
            self.__rec_in_order(cur_node.right)]
            for i in tree:
                to_return = to_return + str(i) +' '
            return to_return

    def pre_order(self):
        string = self.__rec_pre_order(self.__root)
        string = string.split()
        to_return = ''
        for i in string:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_pre_order(self, cur_node):
        to_return = ''
        if cur_node == None:
            return ''
        elif cur_node != None:
            tree = [str(cur_node.value), \
            self.__rec_pre_order(cur_node.left), \
            self.__rec_pre_order(cur_node.right)]
            for i in tree:
                to_return = to_return + str(i) +' '
            return to_return

    def post_order(self):
        string = self.__rec_post_order(self.__root)
        string = string.split()
        to_return = ''
        for i in string:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_post_order(self, cur_node):
        to_return = ''
        if cur_node == None:
            return ''
        elif cur_node != None:
            tree = [self.__rec_post_order(cur_node.left), \
            self.__rec_post_order(cur_node.right), \
            str(cur_node.value)]
            for i in tree:
                to_return = to_return + str(i) +' '
            return to_return

    def breadth_first(self):
    # Construct and return a string representing the breadth-first
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        pass # TODO replace pass with your implementation

    def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
        pass # TODO replace pass with your implementation

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
  bst = Binary_Search_Tree()
  for i in range (2):
      bst.insert_element(2-i)
      bst.insert_element(3+i)
  print (bst)
  bst.remove_element(4)
  print(bst)
  bst.remove_element(1)
  print (bst)
