'''
Given an array of integers, return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

from operator import mul
from functools import reduce

def solution(num_list):
    prod = reduce(mul, num_list)
    sol_list = [ prod/i for i in num_list]
    return sol_list


if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5]
    print('Input : {}'.format(num_list))
    print('Solution is : {}'.format(solution(num_list)))