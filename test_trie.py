#!python

from trie import Trie
import unittest


class TrieTest(unittest.TestCase):

    def test_init(self):
        t = Trie()
        t.insert('abc')
        t.insert('bad')
        t.insert('abcd')
        t.insert('apple')

        assert t.children == {'a': {'p': {'p': {'l': {'e': {}}}}, 'b': {'c': {'d': {}}}}, 'b': {'a': {'d': {}}}}

        assert t.prefix_search('a') == True
        assert t.prefix_search('g') == False


    def test_insert(self):
        t = Trie()
        t.insert('apple')
        assert t.children == {'a': {'p': {'p': {'l': {'e': {}}}}}}
        t.insert('peer')
        assert t.children == {'a': {'p': {'p': {'l': {'e': {}}}}}, 'p': {'e': {'e': {'r': {}}}}}


    def test_prefix_search(self):
        t = Trie()
        t.insert('bear')
        assert t.children == {'b': {'e': {'a': {'r': {}}}}}
        t.insert('big')
        assert t.children == {'b': {'e': {'a': {'r': {}}}, 'i': {'g': {}}}}

        assert t.prefix_search('z') == False
        assert t.prefix_search('b') == True


if __name__ == '__main__':
    unittest.main()
