"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

# Using the sieve of eratosthenes   
# In mathematics, the Sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit.
# ... One of a number of prime number sieves, it is one of the most efficient ways to find all of the smaller primes.
# It may be used to find primes in arithmetic progressions.

def sieve_of_eratosthenes(value, num_list):
    num_list[0] = num_list[1] = False
    for i in range(2, value+1): 
        num_list[i] = True
    p = 2
    while(p*p <= value): 
        if (num_list[p] == True): 
            i = p*2
            while(i <= value): 
                num_list[i] = False
                i += p 
        p += 1


def solution(value):
    # prepare the list of prime numbers then find the smallest pair that constitutes the result.
    num_list = [0]*(value+1)
    sieve_of_eratosthenes(value, num_list)
    val = None
    for i in range(0, value):
        if num_list[i] and num_list[value-i] :
            print(' The sum  {} : {} + {}'.format(value, i, value-i))
            val = i
            break
    if val:
        return val, value-val
    return None,None

solution(18922312)
#The sum  18922312 : 11 + 18922301    
