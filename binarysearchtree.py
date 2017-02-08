
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class BST(object):
    def __init__(self, iterable=None):
        """Initialize this binary search tree and append the given items, if any"""
        self.root = None
        self.count = 0
        if iterable:
            for item in iterable:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BST({})'.format(self.as_list())

    def length(self):
        return self.count

    def is_empty(self):
        return self.root is None

    def insert(self, item):
        self.count += 1
        node = Node(item)
        return insert_helper(item, left, right)

    def insert_helper(self, item, left, right):
        if self.is_empty():
            return self.root = Node(item, None, None)
        elif self.root.data > item:
