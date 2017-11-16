import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester (unittest.TestCase):
    def setUp(self):
        self.__bst = Binary_Search_Tree()
# empty
    def test_empty_bst(self):
        self.assertEqual('[ ]', str(self.__bst))

    def test_empty_bst_height(self):
        self.assertEqual(0, self.__bst.get_height())

    def test_empty_bst_removal(self): # exception
        with self.assertRaises (ValueError):
            self.assertEqual('[ ]', self.__bst.remove_element(1),'Raise ValueError')

    def test_empty_bst_pre_order(self):
        self.assertEqual('[ ]', self.__bst.pre_order())

    def test_empty_bst_post_order(self):
        self.assertEqual('[ ]', self.__bst.post_order())

    def test_empty_bst_breadth_first(self):
        self.assertEqual('[ ]', self.__bst.breadth_first())

    # normal
    def test_insert_one(self):
        self.__bst.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_insert_one_height(self): #########
        self.__bst.insert_element(1)
        self.assertEqual(1, self.__bst.get_height())

    def test_pre_order_one(self):
        self.__bst.insert_element(1)
        self.assertEqual('[ 1 ]', self.__bst.pre_order())

    def test_post_order_one(self):
        self.__bst.insert_element(1)
        self.assertEqual('[ 1 ]', self.__bst.post_order())

    def test_breadth_first_one(self):
        self.__bst.insert_element(1)
        self.assertEqual('[ 1 ]', self.__bst.breadth_first())

    def test_remove_one(self):
        self.__bst.insert_element(1)
        self.__bst.remove_element(1)
        self.assertEqual('[ ]', str(self.__bst))

    def test_remove_one_height(self):
        self.__bst.insert_element(1)
        self.__bst.remove_element(1)
        self.assertEqual(0, self.__bst.get_height())

    def test_romove_one_pre_order(self):
        self.__bst.insert_element(1)
        self.__bst.remove_element(1)
        self.assertEqual('[ ]', self.__bst.pre_order())

    def test_remove_one_post_order(self):
        self.__bst.insert_element(1)
        self.__bst.remove_element(1)
        self.assertEqual('[ ]', self.__bst.post_order())

    def test_remove_one_breadth_first(self):
        self.__bst.insert_element(1)
        self.__bst.remove_element(1)
        self.assertEqual('[ ]', self.__bst.breadth_first())

    def test_insert_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.assertEqual('[ 1, 2 ]', str(self.__bst))

    def test_insert_two_height_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.assertEqual(2, self.__bst.get_height())

    def test_pre_order_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.__bst.pre_order())

    def test_post_order_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.assertEqual('[ 2, 1 ]', self.__bst.post_order())

    def test_breadth_first_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.__bst.breadth_first())

    def test_remove_leaf_with_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_remove_root_with_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', str(self.__bst))

    def test_remove_leaf_with_two_height_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual(1, self.__bst.get_height())

    def test_remove_root_with_two_height_right(self): ####
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual(1, self.__bst.get_height())

    def test_romove_leaf_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.pre_order())

    def test_remove_root_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.pre_order())

    def test_romove_leaf_with_two_post_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.post_order())

    def test_remove_root_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.post_order())

    def test_romove_leaf_with_two_breadth_first_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.breadth_first())

    def test_remove_root_with_two_breadth_first_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.breadth_first())

    #left
    def test_insert_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.assertEqual('[ 0, 1 ]', str(self.__bst))

    def test_insert_two_height_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.assertEqual(2, self.__bst.get_height())

    def test_pre_order_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.assertEqual('[ 1, 0 ]', self.__bst.pre_order())

    def test_post_order_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.assertEqual('[ 0, 1 ]', self.__bst.post_order())

    def test_breadth_first_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.assertEqual('[ 1, 0 ]', self.__bst.breadth_first())

    def test_remove_leaf_with_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_remove_root_with_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', str(self.__bst))

    def test_remove_leaf_with_two_height_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual(1, self.__bst.get_height())

    def test_remove_root_with_two_height_left(self): #########
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual(1, self.__bst.get_height())

    def test_romove_leaf_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.pre_order())

    def test_remove_root_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.pre_order())

    def test_romove_leaf_with_two_post_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.post_order())

    def test_remove_root_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.post_order())

    def test_romove_leaf_with_two_breadth_first_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.breadth_first())

    def test_remove_root_with_two_breadth_first_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.breadth_first())

    # special & (general) exception cases (test on the margin)

    def test_add_four_remove_four_print(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(4)
        self.__bst.remove_element(2)
        self.__bst.remove_element(1)
        self.__bst.remove_element(3)
        self.__bst.remove_element(4)
        self.assertEqual('[ ]', str(self.__bst))

    def test_add_eight_remove_eight_print(self):
        for i in range (4):
            self.__bst.insert_element(4+i)
            self.__bst.insert_element(3-i)
        for i in range (8):
            self.__bst.remove_element(i)
        self.assertEqual('[ ]', str(self.__bst))

    def test_remove_leaf_height(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(4)
        self.__bst.remove_element(4)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_node_with_one_child_print(self):
        for i in range (4):
            self.__bst.insert_element(4+i)
            self.__bst.insert_element(3-i)
        self.__bst.remove_element(5)
        self.assertEqual('[ 0, 1, 2, 3, 4, 6, 7 ]', str(self.__bst))

    def test_remove_node_with_one_child_height(self):
        for i in range (4):
            self.__bst.insert_element(4+i)
            self.__bst.insert_element(3-i)
        self.__bst.remove_element(5)
        self.assertEqual(5, self.__bst.get_height())

    def test_remove_node_with_two_children_print(self):
        for i in range (4):
            self.__bst.insert_element(4+i)
            self.__bst.insert_element(3-i)
        self.__bst.insert_element(4.5)
        self.__bst.remove_element(5)
        self.assertEqual('[ 0, 1, 2, 3, 4, 4.5, 6, 7 ]', str(self.__bst))

    def test_remove_node_with_two_children_height(self):
        for i in range (4):
            self.__bst.insert_element(4+i)
            self.__bst.insert_element(3-i)
        self.__bst.insert_element(4.5)
        self.__bst.remove_element(5)
        self.assertEqual(5, self.__bst.get_height())

    def test_remove_non_existing_value(self):
        with self.assertRaises(ValueError):
            for i in range (4):
                self.__bst.insert_element(4+i)
                self.__bst.insert_element(3-i)
            self.__bst.remove_element(9)

    def test_remove_value_exceeding_volume(self):
        with self.assertRaises(ValueError):
                for i in range (4):
                    self.__bst.insert_element(4+i)
                    self.__bst.insert_element(3-i)
                for i in range(8):
                    self.__bst.remove_element(i)
                self.__bst.remove_element(0)

if __name__ == '__main__':
    unittest.main()
