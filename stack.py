#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # initialize instance variables
        self.stack = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        if self.stack.count == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack"""
        return self.stack.count

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        return self.stack.tail.data

    def push(self, item):
        """Push the given item onto this stack"""
        self.stack.append(item)

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.stack.count == 0:
            raise ValueError
        else:
            top_item = self.stack.tail.data
            self.stack.delete(top_item)
            return top_item
