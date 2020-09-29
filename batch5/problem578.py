"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""
import string

class Solution():
    def __init__(self, primary_word, secondary_word):
        self.primary_word = primary_word
        self.secondary_word = secondary_word

    @staticmethod
    def check_one_to_one_mapping(word_1, word_2):
        status = False
        if len(word_1) != len(word_2):
            return status

        char_map = string.ascii_lowercase
        for index, char in enumerate(word_1):
            loc = char_map.find(char)
            if loc == 25:
                loc = -1
            if char_map[loc+1] != word_2[index]:
                status = False
                break
        else:
            status = True
        return status

    def solve(self):
        status = self.check_one_to_one_mapping(self.primary_word, self.secondary_word)
        if status:
            print("The words are mapped one to one. {} ---> {}".format(self.primary_word, self.secondary_word))
        else:
            print("The words are not mapped one to one.{} ---> {}".format(self.primary_word, self.secondary_word))
        return status


s = Solution('abc', 'bcd')
s.solve()

s = Solution('foo', 'bar')
s.solve()