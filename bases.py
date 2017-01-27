#!python

import string


def decode(str_num, base):
    """
    Decode given number from given base to base 10.
    str_num -- string representation of number in given base
    base -- base of given number
    """
    hex_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16,
    'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24,
    'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32,
    'x': 33, 'y': 34, 'z': 35}

    assert 2 <= base <= 36
    # Decode number
    exp = len(str_num) - 1
    decode_num = 0
    for i in str_num:
        if i.isdigit():
            decode_num += (int(i) * (base ** exp))
        else:
            decode_num += (hex_dict[i] * (base ** exp))
        exp -= 1
    return decode_num

def encode(num, base):
    """
    Encode given number from base 10 to given base.
    num -- the number in base 10
    base -- base to convert to
    """
    hex_digit = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g',
    17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o',
    25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w',
    33: 'x', 34: 'y', 35: 'z'}

    assert 2 <= base <= 36
    encoded_str = ''
    while num > 0:
        remainder = num % base
        divide = num / base
        num = divide
        if base > 10:
            if remainder in hex_digit:
                encoded_str = hex_digit[remainder] + encoded_str
            else:
                encoded_str = str(remainder) + encoded_str
        else:
            encoded_str = str(remainder) + encoded_str
    return encoded_str


def convert(str_num, base1, base2):
    """
    Convert given number from base1 to base2.
    """
    assert 2 <= base1 <= 36
    assert 2 <= base2 <= 36
    # TODO: Convert number
    converted_num = decode(str_num, base1)
    converted_num = encode(converted_num, base2)

    return converted_num



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        str_num = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(str_num, base1, base2)
        print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
    else:
        print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
