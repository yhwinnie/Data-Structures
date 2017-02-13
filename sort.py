#!python

from linkedlist import LinkedList, Node

class Sort(object):


    def __init__(self, arr=None):
        """Initialize this node with the given data"""
        self.arr = arr

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Sort({})'.format(repr(self.arr))

    def check_if_sorted(self, new_arr):
        # O(n)
        for index in range(len(self.arr) - 1):
            if new_arr[index] > new_arr[index + 1]:
                return False
        return True

    def swap(self, i, j, new_arr):
        new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

    def bubble_sort(self):
        # O(n^2)
        # Omega (n)
        new_arr = self.arr
        check_sorted = self.check_if_sorted(new_arr)
        while not check_sorted:
            for index in range(len(self.arr) - 1):
                if new_arr[index] > new_arr[index + 1]:
                    self.swap(index, index + 1, new_arr)
                check_sorted = self.check_if_sorted(new_arr)
        self.arr = new_arr

    def insertion_sort(self):
        # O(n^2)
        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                self.swap(i, i + 1, self.arr)
                for j in range(0, i):
                    if self.arr[j] > self.arr[i]:
                        self.swap(j, i, self.arr)

    def selection_sort(self):
        # O(n^2)
        # Omega (n^2)
        # Theta (n^2)
        if self.arr == []:
            return
        for i_index in range(len(self.arr) - 1):
            min_val, min_index = self.arr[i_index], i_index
            for j_index in range(i_index + 1, len(self.arr)):
                if self.arr[j_index] < min_val:
                    min_val, min_index = self.arr[j_index], j_index
            if self.arr[i_index] > self.arr[min_index]:
                self.swap(i_index, min_index, self.arr)

    def get_range(self):
        max_num, min_num = None, None
        for item in self.arr:
            if max_num is None or min_num is None:
                max_num, min_num = item, item
            else:
                if item > max_num:
                    max_num = item
                elif item < min_num:
                    min_num = item
        return max_num, min_num


    def counting_sort(self):
        if self.arr == []:
            return
        max_range_num, min_range_num = self.get_range()
        count_arr = [0]*(max_range_num + 1)

        for index in range(len(self.arr)):
            count_arr[self.arr[index]] += 1

        for index in range(len(count_arr)):
            if index > 0:
                count_arr[index] = count_arr[index] + count_arr[index - 1]

        sorted_arr = [0] * len(self.arr)

        for index in range(len(self.arr)):
            sorted_arr[count_arr[self.arr[index]] - 1] = self.arr[index]
            count_arr[self.arr[index]] = count_arr[self.arr[index]] - 1
        self.arr = sorted_arr

    def bucket_sort(self):
        max_val, min_val = self.get_range()
        bucket_arr = [LinkedList()] * (len(self.arr))
        for item in self.arr:
            index = (item * len(self.arr))/(max_val + 1)
            # go to the index in the arr and put it inside a linked list
            if bucket_arr[index].length() == 0:
                ll = LinkedList([item])
                bucket_arr[index] = ll
            else:
                ll = bucket_arr[index]
                current_node = ll.head
                if ll.length() == 1:

                    if item > current_node.data:
                        ll.append(item)
                    else:
                        ll.prepend(item)
                else:
                    prev_node = 0
                    while current_node is not None:
                        # get the largest prev_node that is smaller than item
                        if item >= current_node.data:
                            prev_node = current_node
                        current_node = current_node.next
                    if prev_node != 0:
                        new_node = Node(item)
                        new_node.next = prev_node.next
                        prev_node.next = new_node
                    else:
                        ll.prepend(item)

                bucket_arr[index] = ll

        index = 0
        for ll in bucket_arr:
            if ll.length() == 1:
                self.arr[index] = ll.head.data
                index += 1
            elif ll.length() > 1:
                current_node = ll.head
                while current_node is not None:
                    self.arr[index] = current_node.data
                    current_node = current_node.next
                    index += 1



    def radix_sort(self):
        radix_arr = [0] * 10
        for item in self.arr:
            index = item % 10
            radix_arr[index] += 1

        print(radix_arr)
        for index in range(len(radix_arr) - 1):
            if index > 0:
                radix_arr[index] = radix_arr[index] + radix_arr[index - 1]
        print(radix_arr)

        sorted_arr = [0] * len(self.arr)

        index = len(self.arr) - 1
        while index >= 0:
            radix_index = self.arr[index] % 10
            print(radix_index)
            print(radix_arr[radix_index])
            sorted_arr[radix_arr[radix_index]] = self.arr[index]
            radix_arr[radix_index] -= 1
            index -= 1
        self.arr = sorted_arr

        print(self.arr)

    def cocktail_shaker(self, arr):
        pass

    def shell_sort(self, arr):
        pass


if __name__ == '__main__':
    test_sort()
