"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'
"""

import string
# create the num : alphabet mapping
char_mapping = {num: alpha for num,alpha in zip(range(1,27), list(string.ascii_lowercase))}
def decode(message):
    """
     Decode the message and return the count
     print the possible solutions
    """
    solutions = []
    possiblities= {}
    possiblities[message[0]] = 1
    solutions.append(char_mapping[int(message[0])])
    for i in range(1, len(message)):
        if int(message[i]) >= 0:
            solutions.append(char_mapping[int(message[i])])
            possiblities[i] = possiblities.get(i, 0)+1
        combined_sum = int(message[i]) + (10*int(message[i])) 
        if combined_sum <= 26:
            solutions.append(char_mapping[combined_sum])
            possiblities[i] = possiblities.get(i, 0)+1

    print('The solution is : {}'.format(solutions))
    print('THe possiblities is : {}'.format(possiblities))

decode('111')
