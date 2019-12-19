"""
This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.

Upgrade to premium and get in-depth solutions to every problem.
"""
from itertools import zip_longest
import numpy as np
from typing import List


def find_non_duplicated_integer(l: List[int]) -> int:
    """
    Complexities Speed/Space: O(n) - O(1)
    Find and return the non-duplicated integer in an array of integers where every integer occurs three times
    except for one integer (which only occurs once).
    :param l: input integers list
    :type l: List[int]
    :return: the non-duplicated integer
    :type: int
    """
    sum_mod3 = ''   # O(k) with k = max(len(str_in_base3(n))) (with n in in l) ~ O(1) if k bound/small (in regard of n)
    for n in l:     # O(n)
        # convert entry/input number (base10) into base3 and reverse the weight of bits (for '0' filling after)
        # https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.base_repr.html
        n_b3 = np.base_repr(n, base=3)[::-1]    # type: str
        # update the modulo3 sum of each bits columns
        sum_mod3 = [
            # str((int(a) + int(b)) % 3)
            # for a, b in zip_longest(n_b3, sum_mod3, fillvalue='0')
            str(sum(map(int, z_n_s)) % 3)
            for z_n_s in zip_longest(n_b3, sum_mod3, fillvalue='0')
        ]
    return int(''.join(sum_mod3[::-1]), 3)  # reverse the weight of bits and convert to int


if __name__ == '__main__':
    tests = [
        [[6, 1, 3, 3, 3, 6, 6], 1],
        [[13, 19, 13, 13], 19],
        [[123456789, 123456789, 12345678, 123456789], 12345678]
    ]
    for inputs, result_expected in tests:
        assert find_non_duplicated_integer(inputs) == result_expected