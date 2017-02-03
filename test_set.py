#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        s.add('a')
        s.add('b')
        with self.assertRaises(KeyError):
            s.remove('c')
        s.add('c')
        s.add('d')

        assert s.length() == 4

        s.add('e')
        s.add('f')
        s.add('e')
        s.add('a')

        assert s.length() == 6
        #
        assert s.remove('d') == 'd'
        with self.assertRaises(KeyError):
            s.remove('d')
        assert s.remove('c') == 'c'

        assert s.length() == 4


        # assert s.intersection_update(t) == ['a', 'b', 'c', 'd', 'f']



    #     assert s.peek() is None
    #     assert q.length() == 0
    #     assert q.is_empty() is True
    #
    # def test_init_with_list(self):
    #     q = Queue(['A', 'B', 'C'])
    #     assert q.peek() == 'A'
    #     assert q.length() == 3
    #     assert q.is_empty() is False
    #
    # def test_length(self):
    #     q = Queue()
    #     assert q.length() == 0
    #     q.enqueue('A')
    #     assert q.length() == 1
    #     q.enqueue('B')
    #     assert q.length() == 2
    #     q.dequeue()
    #     assert q.length() == 1
    #     q.dequeue()
    #     assert q.length() == 0
    #
    # def test_peek(self):
    #     q = Queue()
    #     assert q.peek() is None
    #     q.enqueue('A')
    #     assert q.peek() == 'A'
    #     q.enqueue('B')
    #     assert q.peek() == 'A'
    #     q.dequeue()
    #     assert q.peek() == 'B'
    #     q.dequeue()
    #     assert q.peek() is None
    #
    # def test_enqueue(self):
    #     q = Queue()
    #     q.enqueue('A')
    #     assert q.peek() == 'A'
    #     assert q.length() == 1
    #     q.enqueue('B')
    #     assert q.peek() == 'A'
    #     assert q.length() == 2
    #     q.enqueue('C')
    #     assert q.peek() == 'A'
    #     assert q.length() == 3
    #     assert q.is_empty() is False
    #
    # def test_dequeue(self):
    #     q = Queue(['A', 'B', 'C'])
    #     assert q.dequeue() == 'A'
    #     assert q.length() == 2
    #     assert q.dequeue() == 'B'
    #     assert q.length() == 1
    #     assert q.dequeue() == 'C'
    #     assert q.length() == 0
    #     assert q.is_empty() is True
    #     with self.assertRaises(ValueError):
    #         q.dequeue()


if __name__ == '__main__':
    unittest.main()
