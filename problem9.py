'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def solution(num_list):
    current_sum = 0
    prev_sum = 0
    for elem in num_list:
        new_sum = max(prev_sum, current_sum)
        current_sum = prev_sum + elem
        prev_sum = new_sum
    return max(prev_sum, current_sum)

print(solution([2,4,6,2,5]))    
print(solution([5, 1, 1, 5]))    
