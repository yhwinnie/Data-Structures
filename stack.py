#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # initialize instance variables
        # self.stack = LinkedList()
        self.stack = []
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # LinkedList
        # if self.stack.count == 0:
        #     return True
        # return False

        # Array
        if len(self.stack) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack"""
        # LinkedList
        # return self.stack.count

        #Array
        return len(self.stack)

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
        # LinkedList
        # return self.stack.tail.data

        # Array
        return self.stack[self.length() - 1]


    def push(self, item):
        """Push the given item onto this stack"""
        self.stack.append(item)

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        # Linked List
        # if self.is_empty():
        #     raise ValueError
        # else:
        #     top_item = self.stack.tail.data
        #     self.stack.delete(top_item)
        #     return top_item

        # Array
        if self.is_empty():
            raise ValueError
        else:
            return self.stack.pop()
