'''
Given an array of integers, 
find the first missing positive integer in linear time and constant space.
 In other words, find the lowest positive integer that does not exist in the array.
  The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''



def solution(num_list):
    prev = 0
    for elem in num_list:
        if elem <= 0:
            continue
        if elem != prev +1:
            print('Missing positive number : {} ---> {}   missing : {}'.format(prev, elem, prev+1))
            return prev+1
        prev = elem

if __name__ == '__main__':
    input_array = [3, 4, -1, 1]
    # sort the elements in place.
    input_array.sort()
    print('Input array is : {}'.format(input_array))
    print('Solution is : {}'.format(solution(input_array)))