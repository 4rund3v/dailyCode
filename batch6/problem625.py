"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""

class Solution():
    def __init__(self, n):
        self.num = n
        self.binary_num = []
        self.max_occurance = 0
        pass

    @staticmethod
    def get_binary_representation(decimal_num):
        binary_rep = []
        while (decimal_num > 0):
            a = int(float(decimal_num % 2))
            binary_rep.append(a)
            decimal_num = (decimal_num - a) / 2
        return binary_rep[::-1]

    def solve(self):
        self.binary_num = self.get_binary_representation(self.num)
        print("Binary Representation of {} is :-> {}".format(self.num, self.binary_num))
        window = 0
        temp = 0
        if not self.binary_num:
            return self.max_occurance

        j = self.binary_num[0]
        if j == 1:
            temp += 1
        for i in self.binary_num[1:]:
            if i == 1:
                if i == j:
                    temp += 1
                else:
                    j = i
                    temp = 1
            else:
                if temp > window:
                    window = temp
                temp = 0
                j = i
        self.max_occurance = window
        print("Max Occurance of the number 1 is : {}".format(self.max_occurance))
        return self.max_occurance


s = Solution(156)
s.solve()