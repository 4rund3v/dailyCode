"""
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped,
the 3rd and 4th bit should be swapped, and so on.
For example, 10101010 should be 01010101.
11100010 should be 11010001.
Bonus: Can you do this in one line?
"""



def solution(eight_bit_str):
    # use tupel unpacking and swap the digits inplace.
    eight_bit_str = list(eight_bit_str)
    eight_bit_str[::2], eight_bit_str[1::2] = eight_bit_str[1::2], eight_bit_str[::2]
    return ''.join(eight_bit_str)


if __name__ == "__main__":
    eight_bit_num = 11100010
    new_eight_bit_num = int(solution(str(eight_bit_num)))
    print(eight_bit_num)
    print(new_eight_bit_num)
