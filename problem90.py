"""
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform)
"""


import random
import math
def solution(num, num_list):
    while True:
        """
        Gaussian Distribution. Gaussian distribution (also known as normal distribution) is a bell-shaped curve,
        and it is assumed that during any measurement values will follow a normal distribution with an equal
        number of measurements above and below the mean value.
        """
        #rand_num = math.ceil(random.uniform(0, num-1))
        rand_num = random.randint(0,num-1)
        if rand_num not in num_list:
            print('Generated random number : {}'.format(rand_num))
            return rand_num
        else:
            print('Rand num in list, finding another : {}'.format(rand_num))


if __name__ == "__main__":
    solution(50, list(range(0,46)))