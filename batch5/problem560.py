"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


class Solution():
    def __init__(self, items, k):
        self.items = items
        self.k = k

    def solve(self):
        # assuming all positive
        temp = [0]*self.k
        temp[self.items[0]] = 1
        for item in self.items[1:]:
            diff = self.k - item
            if temp[diff] == 1:
                print("{} -> {} + {} . Success ".format(self.k, diff, item))
                break
            else:
                temp[item] = 1
        else:
            print("{} could not be found")

s = Solution(items=[10, 15, 3, 7], k=17)
s.solve()