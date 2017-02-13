#!python

from twothreetree import TTTree
import unittest


class TTTreeTest(unittest.TestCase):

    def test_init(self):
        s = TTTree()
        s.insert(5)
        assert s.pointer.left_child_data == 5
        assert s.pointer.parent_node == None
        s.insert(3)
        assert s.pointer.left_child_data == 3
        assert s.pointer.right_child_data == 5
        s.insert(4)
        assert s.pointer.left_child_data == 4
        assert s.pointer.left_child.left_child_data == 3
        assert s.pointer.right_child.left_child_data == 5
        #assert s.pointer.parent_node.left_child_data == 4



        # s.insert(2)
        # assert s.head.right_child.left == 5
        # assert s.head.left_child.left == 2
        # assert s.head.left == 3







if __name__ == '__main__':
    unittest.main()
