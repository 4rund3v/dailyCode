"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

from functools import reduce

class Solution():
    def __init__(self, num_list, max_num):
        self.num_list = num_list
        self.max_num = max_num
        self.product = 0

    @staticmethod
    def find_max(num_list, max_num):
        results = [0]*max_num
        print(results)
        for i in num_list:
            i = abs(i)
            if i >= results[0]:
                results = results[1:]+[i]
        print("Sorted res {}".format(results))
        return results

    def solve(self):
        if len(self.num_list) < self.max_num:
            return self.product
        items = self.find_max(num_list=self.num_list, max_num=self.max_num)
        # def prod(iterable):
        #     p = 1
        #     for n in iterable:
        #         p *= n
        #     return p
        # self.product = prod(items)
        self.product = reduce(lambda x,y: x*y, items)
        print("Solution is :{}".format(self.product))
        return self.product

s = Solution([10, -10, 20, 7, -9,17, -18, 6, 11, -13], 3)
s.solve()