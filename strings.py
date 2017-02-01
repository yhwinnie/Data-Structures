#!python

import string

def search_string(word, string):
    assert isinstance(word, str)
    assert isinstance(string, str)
    return does_contain_iterative(word, string)
    # return does_contain_recursive(word, string)

def does_contain_iterative(word, string):
    word = word.lower()
    string = string.lower()
    if word == '':
        return True
    len_word = len(word)
    for i in range(len(string)):
        if string[i: len_word] == word:
            return True
        len_word += 1
    return False

def does_contain_recursive(word, string, len_word=0, index=0):
    if word == '':
        return True
    if string[index: len_word] == word:
        return True
    if index > len(string):
        return False
    if len_word == 0:
        len_word = len(word)
        return does_contain_recursive(word, string, len_word, index=0)
    else:
        return does_contain_recursive(word, string, len_word + 1, index + 1)

def is_anagram(str1, str2):
    assert isinstance(str1, str)
    assert isinstance(str2, str)
    # return is_anagram_iterative(text)
    str1 = ''.join(sorted(str1.lower()))
    str2 = ''.join(sorted(str2.lower()))

    if str1 == str2:
        return True
    else:
        return False
    #return is_anagram_recursive(str1, str2)

# def is_anagram_recursive(str1, str2):
#     str1 = ''.join(sorted(str1.lower()))
#     str2 = ''.join(sorted(str2.lower()))
#
#     if str1 == str2:
#         return True
#     else:
#         return False

# def is_anagram_iterative(text):


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # O(n)
    # Implement the is_palindrome function iteratively here

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
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # implement the is_palindrome function recursively here
    # O(n)
    # Omega(1)
    if text == '':
        return True

    # Strip punctuations
    # text = "".join(c for c in text if c not in ('!','.',':','-','?',' ', ','))

    # Make everything lower case
    text = text.lower()

    if left == None or right == None:
        return is_palindrome_recursive(text, 0, len(text) - 1)

    if left >= right:
        return True

    # Check letters
    if not text[left].isalpha():
        return is_palindrome_recursive(text, left + 1, right)

    if not text[right].isalpha():
        return is_palindrome_recursive(text, left, right - 1)

    # mid = (right - left) / 2
    # if right < mid or left > mid:
    #     return True
    if text[left] != text[right]:
        return False
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)


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
