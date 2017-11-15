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
        self.__height = 0

    def rec_insert(self, value, cur_node): # should be correct
        if cur_node == None:
            if cur_node is self.__root:
              self.__height = 1
            return self.__BST_Node(value)
        elif cur_node != None:
            if value < cur_node.value:
                cur_node.left = self.rec_insert(value, cur_node.left)
                cur_node.height = cur_node.left.height + 1
            elif value > cur_node.value:
                cur_node.right = self.rec_insert(value, cur_node.right)
                cur_node.height = cur_node.right.height + 1
            elif value == cur_node.value:
                raise ValueError
            if self.__height < cur_node.height:
                self.__height = cur_node.height
            return cur_node

    def insert_element(self, value):
        self.__root = self.rec_insert(value, self.__root)

    def remove_element(self, value):
        self.__root = self.__rec_remove(value, self.__root)

    def __rec_remove(self, value, cur_node):
        if cur_node == None:
            raise ValueError
        if value < cur_node.value:
            cur_node.left = self.__rec_remove(value, cur_node.left)
            #cur_node.__height -= 1
        elif value > cur_node.value:
            cur_node.right = self.__rec_remove(value, cur_node.right)
            #cur_node.__height -= 1
        elif value == cur_node.value:
            if cur_node.left != None and cur_node.right != None:
                prec = cur_node
                replace_with = cur.right
                while replace_with.left != None:
                    prec = replace_with
                    replace_with = replace_with.left
                current.val = replace_with.val
                prec.left = None
                if prec.right == None:
                    prec.height -= 1
            elif cur_node.right == None:
                cur_node = cur_node.left
                if cur_node != None:
                    cur_node.height -= 1
            elif cur_node.left == None:
                cur_node = cur_node.right
                if cur_node != None:
                    cur_node.height -= 1
#if preceding value has two children, don't update height
#if preceding value has one or zero children, update self.__height if .height == self.__height - 1
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
        string = self.__rec_breadth_first(self.__root, self.__height)
        string = string.split()
        to_return = ''
        for i in string:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

        #this should be a queue--when dequeue enqueue children


    def get_height(self):
        return self.__height

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
  bst = Binary_Search_Tree()
  print(bst.get_height())
  bst.insert_element(10)
  print(bst.get_height())
  for i in range (2):
      bst.insert_element(2-i)
      bst.insert_element(3+i)
  print(bst.get_height())
  print(bst)
  bst.remove_element(4)
  print(bst.get_height())
  print(bst)
  bst.remove_element(1)
  print(bst.get_height())
  print (bst)
