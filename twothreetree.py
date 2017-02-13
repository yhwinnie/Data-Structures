#!python

class Node(object):

    def __init__(self, left=None, right=None):
        """Initialize this node with the given data"""
        self.parent_node = None
        self.left_child_data = left
        self.right_child_data = right
        self.left_child_node = None
        self.mid_child_node = None
        self.right_child_node = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

class TTTree(object):

    def __init__(self, iterable=None):
        """Initialize this 2-3 Tree and append the given items, if any"""
        self.pointer = Node()
        if iterable:
            for item in iterable:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this Trie"""
        return 'TTTree({})'.format(self.children())

    def insert(self, item):
        current_node = self.pointer
        if current_node.parent_node == None:
            # Left child is empty
            if current_node.left_child_data == None:
                current_node = Node(item)
            # right child is empty
            elif current_node.right_child_data == None:
                if item < current_node.left_child_data:
                    temp = current_node.left_child_data
                    current_node.left_child_data = item
                    current_node.right_child_data = temp
            # Both are not empty
            elif current_node.right_child_data != None:
                # this is an item that is in the middle
                if item > current_node.left_child_data and item < current_node.right_child_data:
                    # pass it up to the parent
                    current_node.parent_node = Node(item)
                    current_node.parent_node.left_child = Node(current_node.left_child_data)
                    current_node.parent_node.right_child = Node(current_node.right_child_data)
                    current_node = current_node.parent_node

                # item that is smaller than the left child
                elif item < current_node.left_child_data:
                    temp = current_node.left_child_data
                    current_node.left_child_data = item
                    # pass the temp to parent node
                    current_node.parent_node = Node(temp)
                # item that is bigger than the right child
                elif item < current_node.right_child_data:
                    temp = current_node.right_child_data
                    current_node.right_child_data = item
                    # pass the temp to parent node
                    current_node.parent_node = Node(temp)


        self.pointer = current_node

    def search(self, item):
        pass


if __name__ == '__main__':
    test_tttree()
