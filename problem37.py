"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

"""
chain : Make an iterator that returns elements from the first iterable until it is exhausted,
        then proceeds to the next iterable, until all of the iterables are exhausted
chain.from_iterable : Gets chained inputs from a single iterable argument that is evaluated lazily.
combinations : Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted,
               the combination tuples will be produced in sorted order
"""
if __name__ == "__main__":
    input_set = set([1, 2, 3, 4, 5])
    print('Input data : {}'.format(input_set))
    solution = list(itertools.chain.from_iterable(itertools.combinations(list(input_set), rsize)
                                             for rsize in range(len(list(input_set))+1)))
    print('Solution is : {}'.format(solution))
