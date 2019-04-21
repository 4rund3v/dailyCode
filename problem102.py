"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def solution(num_list, ksum):
    #print('Given Num list is : {}'.format(num_list))
    #print('Given Ksum is : {}'.format(ksum))
    res = []
    for i in range(len(num_list)):
        res = []
        for j in num_list[i:]:
            res.append(j)
            print(res, sum(res))
            if sum(res) <= ksum:
                if sum(res) == ksum:
                    #print('sum matched : {}'.format(res))
                    #print('Sequence which adds up to given sum {} --> is : {}'.format( ksum, res))
                    return res
            else:
                break
    return res


num_list = [1,2,3,4,5,6]
print('Solution is : {}'.format(solution(num_list, 9)))
