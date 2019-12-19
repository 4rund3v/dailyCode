"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
 implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
from random import randint

def rand7(rand5):
    """
    >>> from random import randint
    >>> rand5 = lambda: randint(0, 4)
    >>> rand7 = coding_problem_45(rand5)
    >>> 0 <= rand7 < 7
    True
    """
    rand5 = lambda: randint(0, 4)
    rand7 = 0
    for _ in range(24):
        rand7 = (rand7 * 5 + rand5()) % 7
    return rand7


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)