#!python

from priority_queue import PriorityQueue
import random
import unittest

class TestPriority(unittest.TestCase):
    def test_size_of_empty_priorityQueue(self):
        priority_queue = PriorityQueue()
        assert priority_queue.items.size() == 0

    def test_pop_on_empty_priorityQueue(self):
        priority_queue = PriorityQueue()
        with self.assertRaises(ValueError):
            priority_queue.items.pop()

    def test_insert_and_get_one_item(self):
        priority_queue = PriorityQueue()
        priority_queue.insert(5)
        assert priority_queue.size() == 1
        assert priority_queue.pop() == 5
        assert priority_queue.items.items == []

    def test_insert_and_get_many_items(self):
        priority_queue = PriorityQueue()
        items = [9, 25, 86, 3, 29, 5, 55]
        for index, item in enumerate(items):
            priority_queue.insert(item)
            assert priority_queue.size() == index + 1
            # min_item = min(items[: index + 1])
            # assert heap.get_min() == min_item
        assert priority_queue.size() == len(items)
        assert priority_queue.items.items == [3, 9, 5, 25, 29, 86, 55]

    def test_insert_and_get_many_random_items(self):
        priority_queue = PriorityQueue()
        items = random.sample(range(1000), 50)
        for index, item in enumerate(items):
            priority_queue.insert(item)
            # assert priority_queue.size() == index + 1
            # min_item = min(items[: index + 1])
            # assert priority_queue.pop() == min_item
        assert priority_queue.size() == len(items)

    def test_insert_and_remove_one_item(self):
        priority_queue = PriorityQueue()
        priority_queue.insert(5)
        assert priority_queue.size() == 1
        assert priority_queue.pop() == 5
        assert priority_queue.size() == 0

    def test_insert_and_remove_many_items(self):
        priority_queue = PriorityQueue()
        items = [9, 25, 86, 3, 29, 5, 55]
        for item in items:
            priority_queue.insert(item)
        assert priority_queue.size() == len(items)
        sorted_items = sorted(items)
        for index, item in enumerate(sorted_items):
            min_item = priority_queue.pop()
            assert sorted_items[index] == min_item
        assert priority_queue.size() == 0

    def test_insert_and_remove_many_random_items(self):
            priority_queue = PriorityQueue()
            items = random.sample(range(1000), 50)
            for item in items:
                priority_queue.insert(item)
            assert priority_queue.size() == len(items)
            sorted_items = sorted(items)
            for index, item in enumerate(sorted_items):
                min_item = priority_queue.pop()
                assert sorted_items[index] == min_item
            assert priority_queue.size() == 0

    def test_parent_index(self):
            priority_queue = PriorityQueue()
            with self.assertRaises(IndexError):
                priority_queue.items._parent_index(0)
            assert priority_queue.items._parent_index(1) == 0
            assert priority_queue.items._parent_index(2) == 0
            assert priority_queue.items._parent_index(3) == 1
            assert priority_queue.items._parent_index(4) == 1
            assert priority_queue.items._parent_index(5) == 2
            assert priority_queue.items._parent_index(6) == 2
            assert priority_queue.items._parent_index(7) == 3
            assert priority_queue.items._parent_index(8) == 3
            assert priority_queue.items._parent_index(9) == 4
            assert priority_queue.items._parent_index(10) == 4
            assert priority_queue.items._parent_index(11) == 5
            assert priority_queue.items._parent_index(12) == 5
            assert priority_queue.items._parent_index(13) == 6
            assert priority_queue.items._parent_index(14) == 6

    def test_child_index(self):
            priority_queue = PriorityQueue()
            assert priority_queue.items._left_child_index(0) ==  1
            assert priority_queue.items._right_child_index(0) == 2
            assert priority_queue.items._left_child_index(1) ==  3
            assert priority_queue.items._right_child_index(1) == 4
            assert priority_queue.items._left_child_index(2) ==  5
            assert priority_queue.items._right_child_index(2) == 6
            assert priority_queue.items._left_child_index(3) ==  7
            assert priority_queue.items._right_child_index(3) == 8
            assert priority_queue.items._left_child_index(4) ==  9
            assert priority_queue.items._right_child_index(4) == 10
            assert priority_queue.items._left_child_index(5) ==  11
            assert priority_queue.items._right_child_index(5) == 12
            assert priority_queue.items._left_child_index(6) ==  13
            assert priority_queue.items._right_child_index(6) == 14

if __name__ == '__main__':
    unittest.main()
