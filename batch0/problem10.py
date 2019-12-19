'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

import time
from threading import Timer

def print_hello():
    print('Hello !')


def solution(func, time_n):
    thread = Timer(time_n, func)
    thread.start()


if __name__ == '__main__':
    solution(print_hello, 10)
