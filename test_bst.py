#!python

from binarysearchtree import BST
import unittest


class BSTTest(unittest.TestCase):

    def test_init(self):
        # [1, 4, 2, 7, 8, 9, 10])
        b = BST()
        b.insert(b, 1)

        assert b.length() == 1

        b.insert(b, 4)


        assert b.length() == 2

        b.insert(b, 2)
        #print(b.root.right.data)

        b.insert(b, 7)

        assert b.length() == 4

        b.insert(b, 8)
        b.insert(b, 9)
        b.insert(b, 10)



        b.in_order_traversal(b)















if __name__ == '__main__':
    unittest.main()
