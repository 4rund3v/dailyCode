"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then 
“23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""
import string
import itertools
import operator

def solution(str_num, digit_mapping):
    # using itertools product since we just need to multiply
    #  each of the number-aplhabet to another number-alphabet
    temp_list = [list(digit_mapping[i]) for i in str_num]
    res =  [ ''.join(i) for i in list(itertools.product(*temp_list)) ] 
    return res


if __name__ == '__main__':
    alphabets = string.ascii_lowercase
    # CANT USE THIS CUZ , WELL 7 AND 9 ARE STUPID AND HAVE 4 ELEM EACH !!
    # digit_mapping = {str(i+2): alphabets[(3*i):((i*3)+3)] for i in range(10)}
    digit_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    print('Digit mapping is : {}'.format(digit_mapping))
    str_num = "234"
    print("The solution is :  {}".format(solution(str_num, digit_mapping)))
