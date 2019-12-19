'''
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
 For example, car(cons(3, 4)) returns 3,
  and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
'''

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair_func):
    def first(item_1, item_2):
        return item_1
    return pair_func(first)

def cdr(pair_func):
    def last(item_1, item_2):
        return item_2
    return pair_func(last)

if __name__ == '__main__':
    x = cons(10,11)
    print('Items are : 10, 11')
    print('CAR : {}'.format(car(x)))
    print('CDR : {}'.format(cdr(x))) 