#!python
from linkedlist import LinkedList


class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        # initialize instance variables
        # self.queue = LinkedList()
        self.queue = []

        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        # O(1) for linkedlist and array
        # if self.queue.count == 0:
        #     return True
        # return False

        if len(self.queue) == 0:
            return True
        return False

    def length(self):
        # O(1) for linkedlist and array
        """Return the number of items in this queue"""
        # return self.queue.count
        return len(self.queue)

    def peek(self):
        # O(1) for linkedlist and array
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None
        # return self.queue.head.data
        return self.queue[0]

    def enqueue(self, item):
        # O(1) for linkedlist and array
        """Enqueue the given item into this queue"""
        # enqueue given item
        self.queue.append(item)


    def dequeue(self):
        # O(n) for array
        # O(1) for linkedlist
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError
        else:
            # first_item = self.queue.head.data
            # self.queue.delete(first_item)
            # return first_item

            return self.queue.pop(0)
