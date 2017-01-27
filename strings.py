#!python

import string


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # implement the is_palindrome function iteratively here

    if text == '':
        return True

    # Strip punctuations
    text = "".join(c for c in text if c not in ('!','.',':','-','?',' '))

    # Make everything lower case
    text = text.lower()

    start = 0
    end = len(text) - 1
    mid = (end + start) / 2

    while end >= mid or start <= mid:
        if not text[start].isalpha():
            start += 1
        if not text[end].isalpha():
            end -= 1
        else:
            if text[start] != text[end]:
                return False
        start += 1
        end -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None, mid=None):
    # implement the is_palindrome function recursively here
    if text == '':
        return True

    # Strip punctuations
    text = "".join(c for c in text if c not in ('!','.',':','-','?',' ', ','))

    # Make everything lower case
    text = text.lower()
    if left == None or right == None:
        return is_palindrome_recursive(text, 0, len(text) - 1, 0)

    mid = (right - left) / 2
    if right < mid or left > mid:
        return True
    if text[left] == text[right]:
        return is_palindrome_recursive(text, left + 1, right - 1)
    else:
        return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
