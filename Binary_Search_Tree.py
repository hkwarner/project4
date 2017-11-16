import queue

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

    def get_height(self):
        if self.__root == None:
            return 0
        else:
            return self.__height

    def __str__(self):
        return self.in_order()

if __name__ == '__main__':
  bst = Binary_Search_Tree()
  for i in range (5):
      bst.insert_element(2-i)
      bst.insert_element(3+i)
  print (bst)
  bst.remove_element(4)
  print (bst)
  bst.remove_element(1)
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
