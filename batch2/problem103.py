"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
import re

def solution(char_set, base_string):
    char_str = ""
    for i in char_set:
        char_str += "[{}].*?".format(i)
    str_pattern = r"""{}""".format(char_str)
    print("String pattern is : {}".format(str_pattern))
    print("The given string to search in is : {}".format(base_string))
    substrings = list(re.findall(str_pattern, base_string))
    return substrings

if __name__ == "__main__":
    char_set  = ['a', 'e', 'i']
    base_string = "figehaeci"
    print(min(solution(char_set, base_string)))