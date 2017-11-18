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

    # insertion - check height; printing order
    def test_insert_one(self):
        self.__bst.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_insert_one_height(self):
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

    def test_insert_three(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.assertEqual('[ 1, 2, 3 ]', str(self.__bst))

    def test_insert_three_height(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_three_pre_order(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())

    def test_insert_three_post_order(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())

    def test_insert_three_breadth_first(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.assertEqual('[ 2, 1, 3 ]', self.__bst.breadth_first())

    def test_insert_four(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.assertEqual('[ 2, 3, 4, 6 ]', str(self.__bst))

    def test_insert_four_height(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_four_pre_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.assertEqual('[ 4, 2, 3, 6 ]', self.__bst.pre_order())

    def test_insert_four_post_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.assertEqual('[ 3, 2, 6, 4 ]', self.__bst.post_order())

    def test_insert_four_breadth_first(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.assertEqual('[ 4, 2, 6, 3 ]', self.__bst.breadth_first())
###
    def test_insert_five(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.assertEqual('[ 2, 3, 4, 5, 6 ]', str(self.__bst))

    def test_insert_five_height(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_five_pre_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.assertEqual('[ 4, 2, 3, 6, 5 ]', self.__bst.pre_order())

    def test_insert_five_post_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.assertEqual('[ 3, 2, 5, 6, 4 ]', self.__bst.post_order())

    def test_insert_five_breadth_first(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.assertEqual('[ 4, 2, 6, 3, 5 ]', self.__bst.breadth_first())
###
    def test_insert_eight(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7, 8 ]', str(self.__bst))

    def test_insert_eight_height(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.assertEqual(4, self.__bst.get_height())

    def test_insert_eight_pre_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7, 8 ]', self.__bst.pre_order())

    def test_insert_eight_post_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.assertEqual('[ 1, 3, 2, 5, 8, 7, 6, 4 ]', self.__bst.post_order())

    def test_insert_eight_breadth_first(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(7)
        self.__bst.insert_element(8)
        self.assertEqual('[ 4, 2, 6, 1, 3, 5, 7, 8 ]', self.__bst.breadth_first())

    # removal

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

    # insert two remove right leaf
    def test_remove_leaf_with_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_remove_leaf_with_two_height_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual(1, self.__bst.get_height())

    def test_romove_leaf_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.pre_order())

    def test_romove_leaf_with_two_post_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.post_order())

    def test_romove_leaf_with_two_breadth_first_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1 ]', self.__bst.breadth_first())

    # insert two remove root
    def test_remove_root_with_two_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', str(self.__bst))

    def test_remove_root_with_two_height_right(self): ####
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual(1, self.__bst.get_height())

    def test_remove_root_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.pre_order())

    def test_remove_root_with_two_pre_order_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.post_order())

    def test_remove_root_with_two_breadth_first_right(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(2)
        self.__bst.remove_element(1)
        self.assertEqual('[ 2 ]', self.__bst.breadth_first())

    # insert two remove left leaf
    def test_remove_leaf_with_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', str(self.__bst))

    def test_remove_leaf_with_two_height_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual(1, self.__bst.get_height())

    def test_romove_leaf_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.pre_order())

    def test_romove_leaf_with_two_post_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.post_order())

    def test_romove_leaf_with_two_breadth_first_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(0)
        self.assertEqual('[ 1 ]', self.__bst.breadth_first())

    # insert two on left remove root
    def test_remove_root_with_two_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', str(self.__bst))

    def test_remove_root_with_two_height_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual(1, self.__bst.get_height())

    def test_remove_root_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.pre_order())

    def test_remove_root_with_two_pre_order_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.post_order())

    def test_remove_root_with_two_breadth_first_left(self):
        self.__bst.insert_element(1)
        self.__bst.insert_element(0)
        self.__bst.remove_element(1)
        self.assertEqual('[ 0 ]', self.__bst.breadth_first())

    # remove node with two children
    def test_remove_root_with_three(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1, 3 ]', str(self.__bst))

    def test_remove_root_with_three_height(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.remove_element(2)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_root_with_three_pre_order(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.remove_element(2)
        self.assertEqual('[ 3, 1 ]', self.__bst.pre_order())

    def test_remove_root_with_three_post_order(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.remove_element(2)
        self.assertEqual('[ 1, 3 ]', self.__bst.post_order())

    def test_remove_root_with_three_breadth_first(self):
        self.__bst.insert_element(2)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.remove_element(2)
        self.assertEqual('[ 3, 1 ]', self.__bst.breadth_first())

    # remove node with only left child
    def test_remove_node_with_left_child(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(1)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(6.5)
        self.__bst.remove_element(7)
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 6.5, 8 ]', str(self.__bst))

    def test_remove_node_with_left_child_height(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(3)
        self.__bst.insert_element(1)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(6.5)
        self.__bst.remove_element(7)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_node_with_left_child_pre_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(6.5)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4, 2, 1, 3, 6, 5, 8, 6.5 ]', self.__bst.pre_order())

    def test_remove_node_with_left_child_post_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(5)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(6.5)
        self.__bst.remove_element(7)
        self.assertEqual('[ 1, 3, 2, 5, 6.5, 8, 6, 4 ]', self.__bst.post_order())

    def test_remove_node_with_left_child_breadth_first(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(6.5)
        self.__bst.remove_element(7)
        self.assertEqual('[ 4, 2, 6, 1, 3, 5, 8, 6.5 ]', self.__bst.breadth_first())

    # remove node with only right child
    def test_remove_node_with_right_child(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.remove_element(8)
        self.assertEqual('[ 1, 2, 3, 4, 6, 7, 9, 10 ]', str(self.__bst))

    def test_remove_node_with_right_child_height(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.remove_element(8)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_node_with_right_child_pre_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.remove_element(8)
        self.assertEqual('[ 4, 2, 1, 3, 6, 9, 7, 10 ]', self.__bst.pre_order())

    def test_remove_node_with_right_child_post_order(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.remove_element(8)
        self.assertEqual('[ 1, 3, 2, 7, 10, 9, 6, 4 ]', self.__bst.post_order())

    def test_remove_node_with_right_child_breadth_first(self):
        self.__bst.insert_element(4)
        self.__bst.insert_element(2)
        self.__bst.insert_element(6)
        self.__bst.insert_element(1)
        self.__bst.insert_element(3)
        self.__bst.insert_element(8)
        self.__bst.insert_element(7)
        self.__bst.insert_element(10)
        self.__bst.insert_element(9)
        self.__bst.remove_element(8)
        self.assertEqual('[ 4, 2, 6, 1, 3, 9, 7, 10 ]', self.__bst.breadth_first())

    # exceptions

    def test_insert_same_value(self):
        with self.assertRaises(ValueError):
            self.__bst.insert_element(5)
            self.__bst.insert_element(3)
            self.__bst.insert_element(4)
            self.__bst.insert_element(5)

    def test_remove_non_existing_value(self):
        with self.assertRaises(ValueError):
            self.__bst.insert_element(5)
            self.__bst.insert_element(3)
            self.__bst.insert_element(4)
            self.__bst.remove_element(6)

    def test_remove_value_exceeding_volume(self):
        with self.assertRaises(ValueError):
                for i in range (4):
                    self.__bst.insert_element(4+i)
                    self.__bst.insert_element(3-i)
                for i in range(8):
                    self.__bst.remove_element(i)
                self.__bst.remove_element(0)

    # special margin cases

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

if __name__ == '__main__':
    unittest.main()
