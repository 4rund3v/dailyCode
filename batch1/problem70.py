"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

1 = 19
2 = 28
3 = 37
4 = 46
5 = 55
6 = 64
7 = 73
8 = 82
9 = 91
10 = 100

"""

import itertools 
  
def solution(n): 
    count = 0
    for curr in itertools.count(): 
        sum = 0
        x = curr 
        while(x): 
            sum = sum + x % 10
            x = x // 10
        if (sum == 10): 
            count = count + 1
        if (count == n): 
            return curr 
    return -1
  
if __name__=='__main__': 
    print(solution(10))