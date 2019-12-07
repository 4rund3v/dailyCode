#!/usr/bin/python

"""
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.

Solution using the

Kadane’s Algorithm:

Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
"""

def largest_sub_array_sum(array):
    max_sum_till_now = 0 # max sum while addng up the elements
    max_sum = 0 # max sum overall in the sub array
    for elem in array:
        max_sum_till_now += elem
        if max_sum_till_now <= 0:
            max_sum_till_now = 0
            continue
        if max_sum_till_now > max_sum:
            max_sum = max_sum_till_now
    return max_sum


if __name__ == "__main__":
    print('To find the largest sum of a sub array')
    input_array = [-5, -1, -8, -9]
    solution = largest_sub_array_sum(input_array)
    print('Input data is : {}'.format(input_array))
    print('Solution is : {}'.format(solution))