#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if index > len(array) - 1:
        return None
    elif item == array[index]:
        return index
    return linear_search_recursive(array, item, index+1)
    #pass
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively here
    # O(log n)
    left = 0
    right = len(array) - 1

    while right >= left:
        mid = (right - left) / 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            right = mid - 1
        else:
            left = mid + 1

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
    # O(log n)
    # if array == []:
    #     return None
    if left == None or right == None:
        return binary_search_recursive(array, item, left=0, right=len(array) - 1)

    if right < left:
        return None

    mid = (right + left) / 2

    if array[mid] == item:
        return mid
    elif array[mid] > item:
        return binary_search_recursive(array, item, left, mid - 1)
    else:
        return binary_search_recursive(array, item, mid + 1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests below
