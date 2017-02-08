#!python

# class Node(object):
#
#     def __init__(self, data):
#         """Initialize this node with the given data"""
#         self.data = data
#         self.child = {}
#
#     def __repr__(self):
#         """Return a string representation of this node"""
#         return 'Node({})'.format(repr(self.data))

class Trie(object):

    def __init__(self, iterable=None):
        """Initialize this Trie and append the given items, if any"""
        self.children = {}
        if iterable:
            for word in iterable:
                self.insert(word)

    def __repr__(self):
        """Return a string representation of this Trie"""
        return 'Trie({})'.format(self.children())

    def insert(self, word, index=0, current_child=None):
        if current_child == None:
            current_child = self.children
        if index == len(word):
            return self.children
        current_char = word[index]
        if current_char not in current_child:
            current_child[current_char] = {}
            return self.insert(word, index+1, current_child[current_char])
        else:
            return self.insert(word, index+1, current_child[current_char])

    def prefix_search(self, prefix, children=None):
        if children == None:
            return self.prefix_search_helper(prefix, self.children)
        else:
            return self.prefix_search_helper(prefix, children)

    # def prefix_search_loop(self, prefix, children):
        


    def prefix_search_helper(self, prefix, current_children):
        if current_children == {}:
            return False
        if prefix in current_children:
            return True
        else:
            for child in current_children.values():
                return self.prefix_search(prefix, child)

if __name__ == '__main__':
    test_trie()
