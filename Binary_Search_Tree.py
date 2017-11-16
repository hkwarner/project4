<<<<<<< HEAD
import queue
=======
import random
from Queue import Queue  #can we do this or do we need to write a new Queue?
>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58

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

<<<<<<< HEAD
=======
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

>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58
    def insert_element(self, value):
        self.__root = self.rec_insert(value, self.__root)

    def rec_insert(self, val, t):
        if t == None:
            return self.__BST_Node(val)
        elif t != None:
            if val < t.value:
                t.left = self.rec_insert(val, t.left)
                t.height = t.left.height + 1
            elif val > t.value:
                t.right = self.rec_insert(val, t.right)
                t.height = t.right.height + 1
            elif val == t.value:
                raise ValueError
            self.__height = t.height
            return t

    def remove_element(self, value):
        self.__root = self.__rec_remove(value, self.__root)

    def __rec_remove(self, val, t):
        if t == None:
            raise ValueError
<<<<<<< HEAD
        elif val < t.value:
            t.left = self.__rec_remove(val, t.left)
        elif val > t.value:
            t.right = self.__rec_remove(val, t.right)
        elif val == t.value:
            if t.left != None and t.right != None:
                r = t.right
                while r.left != None:
                    r = r.left
                t.val = r.val
                t.right = self.__rec_remove(r.val, t.right.right)
            elif t.left == None:
                t = t.right
            else:
                t = t.left
        return t
=======
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
>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58


    def in_order(self):
        if self.__root == None:
            return '[ ]'
        str_list = self.__rec_in_order(self.__root).split()
        to_return = ''
        for i in str_list:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_in_order(self, t):
        if t == None:
            return ''
        elif t != None:
            tree = self.__rec_in_order(t.left) + ' ' \
            + str(t.value) + ' ' \
            + self.__rec_in_order(t.right)
            return tree

    def pre_order(self):
        if self.__root == None:
            return '[ ]'
        str_list = self.__rec_pre_order(self.__root).split()
        to_return = ''
        for i in str_list:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_pre_order(self, t):
        if t == None:
            return ''
        elif t != None:
            tree = str(t.value) + ' ' \
            + self.__rec_pre_order(t.left) + ' ' \
            + self.__rec_pre_order(t.right)
            return tree

    def post_order(self):
        if self.__root == None:
            return '[ ]'
        str_list = self.__rec_post_order(self.__root).split()
        to_return = ''
        for i in str_list:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

    def __rec_post_order(self, t):
        if t == None:
            return ''
        elif t != None:
            tree = self.__rec_post_order(t.left) + ' ' \
            + self.__rec_post_order(t.right) + ' ' \
            + str(t.value)
            return tree

    def breadth_first(self):
<<<<<<< HEAD
    # Construct and return a string representing the breadth-first
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
        if self.__root == None:
            return '[ ]'
        q = queue.Queue()
        string = str(self.__root.value)
        q.put(self.__root)
        while q.empty() is False:
            t = q.get()
            if t.left != None:
                q.put(t.left)
                string = string + ', ' + str(t.left.value)
            if t.right != None:
                q.put(t.right)
                string = string + ', ' + str(t.right.value)
        to_return = '[ ' + string + ' ]'
        return to_return
=======
        string = []
        nodes = Queue()
        nodes.enqueue(self.__root)
        while(len(nodes)!=0):
            for len(nodes):
              returned = nodes.dequeue()
              string += str(returned.value)
              nodes.enqueue(returned.left)
              nodes.enqueue(returned.right)
        string = string.split()
        to_return = ''
        for i in string:
            to_return = to_return + i + ', '
        to_return = to_return[0:len(to_return)-2]
        return ('[ ' + to_return + ' ]')

        #this should be a queue--when dequeue enqueue children
        #probably mostly right but haven't tested

>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58

    def get_height(self):
        if self.__root == None:
            return 0
        else:
            return self.__height

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
  bst = Binary_Search_Tree()
<<<<<<< HEAD
  for i in range (5):
=======
  print(bst.get_height())
  bst.insert_element(10)
  print(bst.get_height())
  for i in range (2):
>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58
      bst.insert_element(2-i)
      bst.insert_element(3+i)
  print(bst.get_height())
  print(bst)
  bst.remove_element(4)
<<<<<<< HEAD
  print (bst)
=======
  print(bst.get_height())
  print(bst)
>>>>>>> 065d378f2e3bad2e8c498865f4f56221f9566d58
  bst.remove_element(1)
  print(bst.get_height())
  print (bst)
  print ('pre_order', bst.pre_order())
  print ('post order', bst.post_order())
  print ('breadth_first', bst.breadth_first())
  print ('height:', bst.get_height())

  # empty bst
  print ('---empty test case---')
  emp_bst = Binary_Search_Tree()
  print (emp_bst)
  print ('pre_order', emp_bst.pre_order())
  print ('post order', emp_bst.post_order())
  print ('breadth_first', emp_bst.breadth_first())
  print ('height:', emp_bst.get_height())
