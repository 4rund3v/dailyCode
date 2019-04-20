"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""
import itertools

if __name__ == "__main__":
    data = [1, 2, 3]
    print(list(itertools.permutations(data)))