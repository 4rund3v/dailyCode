"""
Given two strings A and B, return whether or not A can
be shifted some number of times to get B.
"""

import re


def solution(string_a, string_b):
    #if re.match(string_b, string_a, re.I):
    #    print('Yes the {} can be shited left to get {}'.format(string_a, string_b))
    #    return True
    if re.search(string_b, string_a, re.I):
        print('Yes the {} can be shited to get {}'.format(string_a, string_b))
        return True
    return False

if __name__ == '__main__':
    string_a = 'Arun'
    string_b = 'run'
    print('String A : {}'.format(string_a))
    print('string B : {}'.format(string_b))
    print(solution(string_a, string_b))
