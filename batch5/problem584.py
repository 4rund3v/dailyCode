"""
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
 If this is not possible, return None.
For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
"""


class Solution():
    def __init__(self, word):
        word = word.replace(" ", '')
        word = word.lower()
        self.word = word
        self.word_len = len(word)
        self.word_map = {}

    @staticmethod
    def prepare_word_map(word):
        word_map = {}
        for char in word:
            if char in word_map:
                word_map[char] += 1
            else:
                word_map[char] = 1
        return word_map

    @staticmethod
    def check_valid_word_map(word, word_map):
        word_len = len(word)
        max_char_len = int(word_len // 2)
        for char in word_map:
            if word_map[char] > max_char_len:
                return False
        return True

    @staticmethod
    def rearrange_word(word_len, word_map):
        word = []
        for i in range(word_len):
            for char in word_map:
                if word_map[char] <= 0:
                    continue
                if i == 0:
                    word.append(char)
                    word_map[char] -= 1
                    break
                if word[-1] == char:
                    continue
                else:
                    word.append(char)
                    word_map[char] -= 1
        return ''.join(word)

    def solve(self):
        new_word = None
        if self.word:
            self.word_map = self.prepare_word_map(self.word)
            if self.check_valid_word_map(self.word, self.word_map):
                new_word = self.rearrange_word(self.word_len, self.word_map)
                print("Rearranged new word is: {} ".format(new_word))
            else:
                print("Cannot Form new word with given word : {} ".format(self.word))
        return new_word

s = Solution(word="aaabbc")
s.solve()

s = Solution(word="aaab")
s.solve()
