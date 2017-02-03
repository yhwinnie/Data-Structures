#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        s.add('a')
        s.add('b')
        with self.assertRaises(KeyError):
            s.remove('c')
        s.add('c')
        s.add('d')

        assert s.length() == 4

        s.add('e')
        s.add('f')
        s.add('e')
        s.add('a')

        assert s.length() == 6
        #
        assert s.remove('d') == 'd'
        with self.assertRaises(KeyError):
            s.remove('d')
        assert s.remove('c') == 'c'

        assert s.length() == 4

        s.add('g')
        s.add('h')
        s.add('i')
        s.add('j')
        s.add('k')
        s.add('l')
        s.add('m')
        s.add('n')
        s.add('o')
        s.add('p')
        s.add('q')
        s.add('r')
        s.add('s')
        s.add('t')
        s.add('u')
        s.add('v')

        assert s.length() == 20

        s.remove('v')

        s.remove('s')

        assert s.length() == 18

    





if __name__ == '__main__':
    unittest.main()
