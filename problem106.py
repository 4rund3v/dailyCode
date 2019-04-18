"""
Given an integer list where each number represents the number of hops you can make,
 determine whether you can reach to the last index starting at index 0.
For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""

def solution(hops_list):
    current_point = 0
    for index, elem in enumerate(hops_list):        
        if current_point == index:
            # when im on a index, skip over the number of items pointed by that index
            current_point += elem
    return current_point == (len(hops_list)-1)


if __name__ == '__main__':
    hops_list = [2, 0, 1, 0]
    bad_hops_list = [1, 1, 0, 1]
    print('{} ----> : {}'.format(hops_list, solution(hops_list)))
    print('{} ----> : {}'.format(bad_hops_list, solution(bad_hops_list)))