#!python
from heap import MinHeap
from binarysearchtree import BST


class PriorityQueue(object):
    """A PriorityQueue is an unordered collection with access to its minimum item,
    and provides efficient methods for insertion and removal of its minimum."""

    def __init__(self):
        """Initialize this min heap with an empty list of items"""
        self.items = MinHeap()
        # self.items = BST()


    def __repr__(self):
        """Return a string representation of this min heap"""
        return 'PriorityQueue({})'.format(self.items)

    def __len__(self):
        return self.items.size()

    def size(self):
        """Return the number of items in the priority queue"""
        return self.items.size()

    def pop(self):
        return self.items.pop()

    def insert(self, item):
        self.items.insert(item)
