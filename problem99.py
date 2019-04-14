"""
Given an unsorted array of integers, find the length of the longest consecutive elements
sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element
 sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
#todo in O(n) time


def solution(sequence):
    # not O(n), gotta figure it out
    # iterate over the list and find the sequence when sequence breaks,start iterating over it 
    sols = []
    temp = 0
    for i in range(0, len(sequence)):
        sols.append(1)
        if i < sols[temp] -1:
            # if we found 4 elem in a sequence, then we can skip over 
            # the three elements and continue from whenre the sequence broke
            # instead of continuing on it
            continue
        for pos, j in enumerate(sequence[i:]):
            if pos+i+1 < len(sequence):
                if sequence[pos+i+1] == j+1:
                    sols[i] += 1
                    temp = i
    return max(sols)

if __name__ == "__main__" :
    sequence = [100, 4, 200, 1, 3, 2]
    sequence.sort()
    print('Solution is : {}'.format(solution(sequence)))
