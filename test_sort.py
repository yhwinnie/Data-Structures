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
        s = Sort([5, 4, 6, 2, 3])
        s.insertion_sort()
        assert s.arr == [2, 3, 4, 5, 6]

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
        s.counting_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44])
        s.counting_sort()
        assert s.arr == [4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.counting_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.counting_sort()
        assert s.arr == [0, 1]

    def test_bucket_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.bucket_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44])
        s.bucket_sort()
        assert s.arr == [4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.bucket_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.bucket_sort()
        assert s.arr == [0, 1]
        s = Sort([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
        113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 241, 239, 251, 257, 263, 269,
        271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
        359, 367, 373, 379, 383, 769, 397, 401, 409, 419, 421, 431, 433, 439,
        443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
        541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
        719, 727, 733, 739, 743, 751, 757, 761, 389, 773, 787, 797, 809, 811,
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
        911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
        s.bucket_sort()
        assert s.arr == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
        113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
        271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
        359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
        443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
        541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
        719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
        911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        s = Sort([1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        s.bucket_sort()
        assert s.arr == [1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]


    def DISABLE_test_radix_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9])
        s.radix_sort()
        assert s.arr == [1, 2, 4, 7, 8, 9]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        s.radix_sort()
        assert s.arr == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.radix_sort()
        assert s.arr == []
        s = Sort([0, 1])
        s.radix_sort()
        assert s.arr == [0, 1]

    def test_merge_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9, 10])
        assert s.merge_sort([1, 4, 2, 7, 8, 9, 10]) == [1, 2, 4, 7, 8, 9, 10]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        assert s.merge_sort([44, 8, 7, 44, 5, 4, 44, -1]) == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.merge_sort([])
        assert s.merge_sort([]) == []
        s = Sort([0, 1])
        s.merge_sort([0, 1])
        assert s.merge_sort([0, 1]) == [0, 1]


    def DISABLE_test_tree_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9, 10])
        assert s.tree_sort([1, 4, 2, 7, 8, 9, 10]) == [1, 2, 4, 7, 8, 9, 10]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        assert s.tree_sort([44, 8, 7, 44, 5, 4, 44, -1]) == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.tree_sort([])
        assert s.tree_sort([]) == []
        s = Sort([0, 1])
        s.tree_sort([0, 1])
        assert s.tree_sort([0, 1]) == [0, 1]

    def test_stable_quick_sort(self):
        s = Sort([1, 4, 2, 7, 8, 9, 10])
        assert s.quick_stable_sort([1, 4, 2, 7, 8, 9, 10]) == [1, 2, 4, 7, 8, 9, 10]
        s = Sort([44, 8, 7, 44, 5, 4, 44, -1])
        assert s.quick_stable_sort([44, 8, 7, 44, 5, 4, 44, -1]) == [-1, 4, 5, 7, 8, 44, 44, 44]
        s = Sort([])
        s.quick_stable_sort([])
        assert s.quick_stable_sort([]) == []
        s = Sort([0, 1])
        s.quick_stable_sort([0, 1])
        assert s.quick_stable_sort([0, 1]) == [0, 1]









if __name__ == '__main__':
    unittest.main()
