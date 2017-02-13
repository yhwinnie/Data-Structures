#!python

class Sort(object):

    def __init__(self, arr=None):
        """Initialize this node with the given data"""
        self.arr = arr

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Sort({})'.format(repr(self.arr))

    def check_if_sorted(self, new_arr):
        for index in range(len(self.arr) - 1):
            if new_arr[index] > new_arr[index + 1]:
                return False
        return True

    def swap(self, i, j, new_arr):
        new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

    def bubble_sort(self):
        new_arr = self.arr
        check_sorted = self.check_if_sorted(new_arr)
        while not check_sorted:
            for index in range(len(self.arr) - 1):
                if new_arr[index] > new_arr[index + 1]:
                    self.swap(index, index + 1, new_arr)
                check_sorted = self.check_if_sorted(new_arr)
        self.arr = new_arr

    def insertion_sort(self):
        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                self.swap(i, i + 1, self.arr)
                for j in range(0, i):
                    if self.arr[j] > self.arr[i]:
                        self.swap(j, i, self.arr)


    def selection_sort(self):
        if self.arr == []:
            return
        for i_index in range(len(self.arr) - 1):
            min_val, min_index = self.arr[i_index], i_index
            for j_index in range(i_index + 1, len(self.arr)):
                if self.arr[j_index] < min_val:
                    print(self.arr[j_index])
                    min_val, min_index = self.arr[j_index], j_index
            if self.arr[i_index] > self.arr[min_index]:
                self.swap(i_index, min_index, self.arr)

        print(self.arr)

    def counting_sort(self, arr):
        pass

    def bucket_sort(self, arr):
        pass

    def radix_sort(self, arr):
        pass

    def cocktail_shaker(self, arr):
        pass

    def shell_sort(self, arr):
        pass


if __name__ == '__main__':
    test_sort()
