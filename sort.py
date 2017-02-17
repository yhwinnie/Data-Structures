#!python

from linkedlist import LinkedList, Node
from binarysearchtree import BST, Node


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
        return new_arr

    def insertion_sort(self):
        # O(n^2)
        # Omega (n^2) when compared to front
        # Omega (n) compared to back
        # Omega(log n) compared with binary search
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


    def merge_sort(self, arr):
        # O(nlogn)
        # Merge sort recursively calling merge sort
        if len(arr) <= 1:
            return arr
        # O(log n)
        divide = len(arr)/2
        left_lst = self.merge_sort(arr[:divide])
        right_lst = self.merge_sort(arr[divide:])

        return self.merge_sort_helper(left_lst, right_lst)

    def merge_sort_helper(self, array_one, array_two):
        # O(n)
        sorted_lst = []
        while len(array_one) != 0 and len(array_two) != 0:
            if array_one[0] >= array_two[0]:
                sorted_lst.append(array_two.pop(0))
            else:
                sorted_lst.append(array_one.pop(0))

        if array_one:
            sorted_lst.extend(array_one)

        if array_two:
            sorted_lst.extend(array_two)

        return sorted_lst

    def quick_stable_sort(self, arr):
        if len(arr) <= 2:
            return arr
        pivot = arr[len(arr) - 1]
        pivot_index = len(arr) - 1
        left_index = 0
        right_index = len(arr) - 2
        return self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)

    def quick_stable_sort_helper(self, pivot, pivot_index, left_index, right_index, arr):
        print(arr)
        print(right_index)
        print(left_index)
        pivot = arr[pivot_index]
        print("PIVOT")
        print(pivot)
        if left_index == right_index:
            if arr[right_index] > pivot:
                print("HERE")
                arr[right_index], arr[pivot] = arr[pivot], arr[right_index]
                pivot_index = right_index
                right_index = pivot_index - 1
                self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)
                right_index = len(arr) - 1
                left_index = pivot_index + 1
                self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)

        elif arr[left_index] > pivot and arr[right_index] < pivot:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            self.quick_stable_sort_helper(pivot, pivot_index, left_index + 1, right_index - 1)
        elif arr[left_index] > pivot and arr[right_index] >= pivot:
            right_index -= 1
            self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)
        elif arr[left_index] < pivot and arr[right_index] <= pivot:
            left_index += 1
            self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)
        else:
            right_index -= 1
            left_index += 1
            self.quick_stable_sort_helper(pivot, pivot_index, left_index, right_index, arr)


        return arr

    def tree_sort(self, arr):
        #O(nlogn)
        b_search_tree = BST()
        # Insert into Binary Search Tree
        #O(n) to go through the array
        for item in arr:
            # O(log n) to put in the item
            b_search_tree.insert(b_search_tree, item)

        # After that, traverse the binary search tree in order and
        # return the sorted lst.
        # O(n) to traverse?
        #print(b_search_tree.in_order_traversal(b_search_tree))
        return b_search_tree.in_order_traversal(b_search_tree)

    # Stretch Challenges
    def radix_sort(self):
        radix_arr = [0] * 10
        for item in self.arr:
            index = item % 10
            radix_arr[index] += 1

        #print(radix_arr)
        for index in range(len(radix_arr) - 1):
            if index > 0:
                radix_arr[index] = radix_arr[index] + radix_arr[index - 1]
        #print(radix_arr)

        sorted_arr = [0] * len(self.arr)

        index = len(self.arr) - 1
        while index >= 0:
            radix_index = self.arr[index] % 10
            #print(radix_index)
            #print(radix_arr[radix_index])
            sorted_arr[radix_arr[radix_index]] = self.arr[index]
            radix_arr[radix_index] -= 1
            index -= 1
        self.arr = sorted_arr

        #print(self.arr)

    def cocktail_shaker(self):
        pass

    def shell_sort(self):
        pass

if __name__ == '__main__':
    test_sort()
