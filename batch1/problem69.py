"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
import sys 
def maxProduct(arr, n): 
    if n < 3: 
        return -1
    max_product = -(sys.maxsize - 1) 
    # max_product is now least negative number
    for i in range(0, n - 2): 
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n): 
                max_product = max( 
                    max_product, arr[i] 
                    * arr[j] * arr[k]) 
    return max_product 
  
if __name__ == "__main__":
    num_arr = [10, 3, 5, 6, 20] 
    num_arr = [-10, -10, 5, 2]
    n = len(num_arr)
    max = maxProduct(num_arr, n) 
    if max == -1: 
        print("No Tripplet Exits") 
    else: 
        print("Maximum product is", max)