#!python

from sort import Sort
import unittest


class SortTest(unittest.TestCase):

    def test_init(self):
        s = Sort([1, 2, 5, 7, 8, 3, 4])
        assert s.check_if_sorted([1, 2, 5, 7, 8, 3, 4]) == False
        s = Sort([1, 2, 3, 4, 5, 6, 7])
        assert s.check_if_sorted([1, 2, 3, 4, 5, 7, 8]) == True
        s = Sort([])
        assert s.check_if_sorted([]) == True


    def test_bubble_sort(self):
        s = Sort([1, 2, 5, 7, 8, 3, 4])
        s.bubble_sort()
        assert s.arr == [1, 2, 3, 4, 5, 7, 8]
        s = Sort([])
        s.bubble_sort()
        assert s.arr == []
        s = Sort([9, 8, 7, 6, 5, 4, 3, -1])
        s.bubble_sort()
        assert s.arr == [-1, 3, 4, 5, 6, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.bubble_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]

    def test_insertion_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.insertion_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.insertion_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.insertion_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.insertion_sort()
        assert s.arr == [0, 1]

    def test_selection_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.selection_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.selection_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.selection_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.selection_sort()
        assert s.arr == [0, 1]

    def test_counting_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.selection_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.selection_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.selection_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.selection_sort()
        assert s.arr == [0, 1]

    def test_bucket_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.selection_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.selection_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.selection_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.selection_sort()
        assert s.arr == [0, 1]

    def test_radix_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.selection_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.selection_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.selection_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.selection_sort()
        assert s.arr == [0, 1]

    







if __name__ == '__main__':
    unittest.main()
