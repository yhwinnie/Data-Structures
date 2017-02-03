#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.bucket_size = init_size
        self.buckets = [LinkedList() for i in range(init_size)]
        self.prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
        113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
        271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
        359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
        443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
        541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
        719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811,
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
        911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        # Count number of key-value entries in each of the buckets
        """Return the length of this hash table by traversing its buckets
        - Best case: omega(n): Need to traverse the bucket list and if
        all the linkedlists are empty.
        - Worst case: O(n^2): Need to traverse the bucket list and the
        linkedlist to find the length"""

        count = 0
        for ll in self.buckets:
            current = ll.head
            count += ll.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False
        - Best case: omega(1): If the key exists and is at the beginning of
        linkedlist.
        - Worst case: O(n): If the key is in the middle and end of the linkedlist
        """
        # Check if the given key exists in a bucket
        index = self._bucket_index(key)
        ll = self.buckets[index]
        current = ll.head
        while current is not None:
            if current.data[0] == key:
                return True
            else:
                current = current.next
        return False

    def resize(self):
        # O(n) where n is the size of prime_numbers list
        old_buckets = self.buckets

        double_size = self.buckets * 2
        for prime_num in range(len(self.prime_numbers) - 1):
            if (double_size >= self.prime_numbers[prime_num] and double_size < self.prime_numbers[prime_num + 1]):
                self.bucket_size = self.prime_numbers[prime_num + 1]
                HashTable(self.bucket_size)
                return

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError
        - Best case: omega(1): If the linkedlist inside the bucket is empty or
        it only has one item.
        - Worst case: O(n^2): if linkedlist inside the bucket is long and the key
        is either in the middle or the end of the list."""
        # Check if the given key exists and return its associated value
        index = self._bucket_index(key)
        ll = self.buckets[index]
        if self.contains(key):
            current = ll.head
            while current is not None:
                if current.data[0] == key:
                    return current.data[1]
                else:
                    current = current.next
        else:
            raise KeyError

    def set(self, key, value):
        """Insert or update the given key with its associated value
        - Best case: omega(1): Access the tail and input the item.
        - Worst case: O(n): Access the tail and input the item."""
        # Insert or update the given key-value entry into a bucket

        load_factor = self.length()/self.bucket_size

        if load_factor > 0.75:
            self.resize()

        index = self._bucket_index(key)
        ll = self.buckets[index]

        item = [key, value]
        current = ll.head
        if current is None:
            ll.append(item)
        elif not self.contains(key):
            ll.append(item)
        else:
            find = ll.find(lambda x: x[0] == key)
            if find is not None:
                ll.delete(find)
                ll.append([key, value])


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError
        Insert or update the given key with its associated value
        - Best case: omega(1)
        - Worst case: O(n)"""
        # Find the given key and delete its entry if found

        if not self.contains(key):
            raise KeyError
        else:
            index = self._bucket_index(key)
            ll = self.buckets[index]
            value = self.get(key)
            return ll.delete([key, value])

    def keys(self):
        """Return a list of all keys in this hash table
        - Best case: omega(n)
        - Worst case: O(n^2)"""
        # Collect all keys in each of the buckets
        lst = []
        for ll in self.buckets:
            current = ll.head
            while current is not None:
                lst.append(current.data[0])
                current = current.next
        return lst

    def values(self):
        """Return a list of all values in this hash table
        - Best case: omega(n)
        - Worst case: O(n^2)"""
        # Collect all values in each of the buckets
        lst = []
        for ll in self.buckets:
            current = ll.head
            while current is not None:
                lst.append(current.data[1])
                current = current.next
        return lst
