"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""
class Solution():
    def __init__(self, items):
        self.items = items

    def solve(self):
        sorted_list = []
        neg_squares = []
        pos_squares = []
        for item in self.items:
            if item < 0:
                neg_squares.append(item*item)
            else:
                pos_squares.append(item*item)
        neg_squares = neg_squares[::-1] # cuz neg numbers squares are reversed
        i = 0
        j = 0
        while i < len(neg_squares) and j < len(pos_squares):
            if neg_squares[i] < pos_squares[j]:
                sorted_list.append(neg_squares[i])
                i += 1
            else:
                sorted_list.append(pos_squares[j])
                j += 1
        sorted_list = sorted_list + neg_squares[i:] + pos_squares[j:]
        print("Sorted list is : {} ".format(sorted_list))
        return sorted_list

s = Solution(items=[-9, -2, 0, 2, 3])
s.solve()
