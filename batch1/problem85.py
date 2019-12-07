"""
Given three 32-bit integers x, y, and b,
 return x if b is 1
 and y if b is 0,
using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""

def gimme_val(x, y, b):
    # returns x if b is one
    # returns y if b is 0
    # using only mathematical operations ??
    if b & 1:
        return x
    else: 
        return y


x = 12345 
y = 67890
b = 1
print(gimme_val(x, y, b))