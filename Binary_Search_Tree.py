from Queue import Queue

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

    def rec_insert(self, value, t):
        if t == None: # base
            t = self.__BST_Node(value)
            t.height = 1
        elif t != None:
            if value < t.value: # left
                t.left = self.rec_insert(value, t.left)
            elif value > t.value: # right
                t.right = self.rec_insert(value, t.right)
            elif value == t.value:
                raise ValueError
            # adjust tree height
            if t.right == None:
                t.height = t.left.height + 1
            elif t.left == None:
                t.height = t.right.height + 1
            elif t.left.height > t.right.height:
                t.height = t.left.height + 1
            else:
                t.height = t.right.height + 1 
        # update root height when necessary
        if t.height > self.__height:
            self.__height = t.height
        return t

    def remove_element(self, value):
        self.__root = self.__rec_remove(value, self.__root)

    def __rec_remove(self, value, t):
        if t == None:
            raise ValueError
        elif t != None:
            if value == t.value: # value found
                if t.left != None and t.right != None: # two children
                    r = t.right
                    while r.left != None: # find min on right
                        r = r.left
                    t.value = r.value
                    t.right = self.__rec_remove(r.value, t.right)
                elif t.left == None: # one or no child
                    t = t.right
                else:
                    t = t.left
            elif value < t.value: # left
                t.left = self.__rec_remove(value, t.left)
            elif value > t.value: # right
                t.right = self.__rec_remove(value, t.right)
            # adjust tree height
            if t != None:
                if t.left == None and t.right == None:
                    t.height = 1
                elif t.left != None and t.right != None:
                    if t.left.height > t.right.height:
                        t.height = t.left.height + 1
                    else:
                        t.height = t.right.height + 1
                elif t.right == None:
                    t.height = t.left.height + 1
                else:
                    t.height = t.right.height + 1
        # update root height if necessary
        if t != None and self.__height - t.height == 1:
            self.__height = t.height
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
        if self.__root == None:
            return '[ ]' # empty case
        q = Queue()
        string = str(self.__root.value)
        q.enqueue(self.__root)
        while len(q) > 0 :
            t = q.dequeue()
            if t.left != None:
                q.enqueue(t.left)
                string = string + ', ' + str(t.left.value)
            if t.right != None:
                q.enqueue(t.right)
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

# if __name__ == '__main__':
#   bst = Binary_Search_Tree()
#   bst.insert_element(3)
#   bst.insert_element(2)
#   print (bst)
#   bst.remove_element(3)
#   print (bst)
#   print ('height', bst.get_height())
