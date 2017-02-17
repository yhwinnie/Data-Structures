
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

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BST({})'.format(self.root)

    def __iter__(self):
        return self.root.__iter__()

    def length(self):
        return self.count

    def is_empty(self):
        return self.root is None

    def insert(self, tree, item):
        self.count += 1
        if tree.root is None:
            tree.root = Node(item)
        else:
            self.insert_helper(tree.root, item)

    def insert_helper(self, node, item):
        if node.data >= item:
            if node.left is None:
                node.left = Node(item)
            else:
                self.insert_helper(node.left, item)
        else:
            if node.right is None:
                node.right = Node(item)
            else:
                self.insert_helper(node.right, item)


    def in_order_traversal(self, tree):
        sorted_lst = []
        if tree.root is None:
            return None
        else:
            self.in_order_traversal_helper(tree.root, sorted_lst)


    def in_order_traversal_helper(self, node, sorted_lst):
        print(node.data)
        #sorted_lst.append(node.data)

        if node.left is not None:
            self.in_order_traversal_helper(node.left, sorted_lst)
            #print(node.data)
            sorted_lst.append(node.data)
    
        if node.right is not None:
            #print(node.data)
            sorted_lst.append(node.data)
            self.in_order_traversal_helper(node.right, sorted_lst)
        else:
            sorted_lst.append(node.data)
        print(sorted_lst)
        return sorted_lst
