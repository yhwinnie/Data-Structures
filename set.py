#!python
from hashtable import HashTable


class Set(object):

    def __init__(self, iterable=None):
        """Initialize this set with the given items, if any"""
        # initialize instance variables
        self.hash = HashTable()
        if iterable:
            for item in iterable:
                self.add(item)


    def __repr__(self):
        """Return a string representation of this set"""
        return 'Set({})'.format(self.hash.length())


    def length(self):
        return self.hash.length()


    def add(self, item):
        # O(n)
        """add element item to set s"""
        #key = self.hash._bucket_index(item)
        if not self.hash.contains(item):
            self.hash.set(item, None)

    def remove(self, item):
        # O(n)
        """remove x from set s; raises KeyError if not present"""
        if not self.hash.contains(item):
            raise KeyError
        else:
            self.hash.delete(item)
            return item



    # def pop(self):
    #     """remove and return an arbitrary element from s; raises KeyError if empty"""
    #     if self.hash.length == 0:
    #         raise KeyError
    #     else:
    #         return
    #
    # def discard(self, key):
    #     """removes x from set s if present"""
    #     if self.hash.contains(key):
    #         self.hash.delete(key)
    #
    # def clear(self):
    #     """remove all elements from set s"""
    #     pass
    #
    # def update(self):
    #     """return set s with elements added from t"""
    #     pass
    #
    # def intersection_update(self, t):
    #     """return set s keeping only elements also found in t"""
    #     for element in t.hash.buckets:
    #         if not self.hash.contains(element):
    #             self.add(element)
    #     print(self.hash.values())
    #     return self.hash.values()
    #
    # def difference_update(self):
    #     """return set s after removing elements found in t"""
    #     pass
    #
    # def symmetric_difference_update(self):
    #     """return set s with elements from s or t but not both"""
    #     pass
