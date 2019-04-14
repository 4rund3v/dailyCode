"""
Implement division of two positive integers without using the division,
multiplication, or modulus operators. Return the quotient as an integer,
ignoring the remainder.
"""
def return_quotient(a, b):
    # keep subtracting, n number of times
    # assuming a & b are > than 0 and a > b
    quotient = 0
    temp = a
    while(temp >= b):
        temp -= b
        quotient += 1
    if temp>0:
        print('remainder is : {}'.format(temp))
    return quotient

print('quotient is : {}'.format(return_quotient(1920293, 7)))
#remainder is : 4
#quotient is : 274327