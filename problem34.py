'''
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
'''

"""
Recursive Solution:
The minimum number of insertions in the string str[l…..h] can be given as:
minInsertions(str[l+1…..h-1]) if str[l] is equal to str[h]
min(minInsertions(str[l…..h-1]), minInsertions(str[l+1…..h])) + 1 otherwise
Dynamic Programming:
If we observe the above approach carefully, we can find that it exhibits
overlapping subproblems.
Suppose we want to find the minimum number of insertions in string “abcde”:
                  abcde
            /       |       \
           /        |         \
           bcde         abcd       bcd  <- case 3 is discarded as str[l] != str[h]
       /   |   \       /   |    \
      /    |    \     /    |     \
     cde   bcd  cd   bcd abc bc
   / | \  / | \ /|\ / | \
de cd d cd bc c………………….
The substrings (bcd) show that the recursion to be terminated and the recursion
tree cannot originate from there. Substring in the same color indicates
overlapping subproblems.
How to reuse solutions of subproblems?
We can create a table to store results of subproblems so that they can be used
directly if same subproblem is encountered again.
The below table represents the stored values for the string abcde.
a b c d e
----------
0 1 2 3 4
0 0 1 2 3
0 0 0 1 2
0 0 0 0 1
0 0 0 0 0
How to fill the table?
The table should be filled in diagonal fashion. For the string abcde, 0….4, the
following should be order in which the table is filled:
Gap = 1:
(0, 1) (1, 2) (2, 3) (3, 4)
Gap = 2:
(0, 2) (1, 3) (2, 4)
Gap = 3:
(0, 3) (1, 4)
Gap = 4:
(0, 4)
"""


# A Naive recursive program to find minimum  
# number insertions needed to make a string 
# palindrome 
import sys 
  
# Recursive function to find minimum  
# number of insertions 
def findMinInsertions(str, l, h): 
  
    # Base Cases 
    if (l > h): 
        return sys.maxsize 
    if (l == h): 
        return 0
    if (l == h - 1): 
        return 0 if(str[l] == str[h]) else 1
  
    # Check if the first and last characters are 
    # same. On the basis of the comparison result,  
    # decide which subrpoblem(s) to call 
      
    if(str[l] == str[h]): 
        return findMinInsertions(str, l + 1, h - 1) 
    else: 
        return (min(findMinInsertions(str, l, h - 1), 
                    findMinInsertions(str, l + 1, h)) + 1) 
  
# Driver Code 
if __name__ == "__main__": 
      
    str = "geeks"
    print(findMinInsertions(str, 0, len(str) - 1)) 
  
# This code is contributed by ita_c 