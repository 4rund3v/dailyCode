"""
Given a string of parentheses, write a function to compute the minimum
number of parentheses to be removed to make the string valid
 (i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""

def num_of_parenthesis_to_remove(base_string):
    to_remove = 0
    open_count = 0 
    close_count = 0
    for i in base_string:
        if i == '(':
            open_count += 1
        elif i == ')':
            close_count += 1
            if close_count > open_count:
                to_remove += 1
                close_count -= 1
    to_remove += abs(open_count - close_count)
    return to_remove


base_string = "()())()"
print('string is : {} ----> {}'.format(base_string, num_of_parenthesis_to_remove(base_string)))

base_string_2 = ")("
print('string is : {} ---> {}'.format(base_string_2, num_of_parenthesis_to_remove(base_string_2)))