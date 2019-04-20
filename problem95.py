"""
Given a number represented by a list of digits,
 find the next greater permutation of a number,
  in terms of lexicographic ordering.
   If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3].
 The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

def solution(num_list):
   max = num_list[0]
   min = num_list[0]
   for i in num_list:
      if i > max:
         max = i
      if i < min:
         min = i
   if min == max:
      # same elements
      return num_list
   if max == num_list[0]:
      return num_list.sort(,reverse=True)
   if 
   return num_list


if __name__ == "__main__":
    num_list = [1, 2, 3]
    print(solution(num_list))
    pass