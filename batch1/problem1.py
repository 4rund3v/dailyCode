'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def solution(num_list, ksum):
    solutions = set()
    for i in num_list:
        if ksum-i in solutions:
            print('Solution is :  {} ---> {} + {}'.format(ksum, i, ksum-i))
            return True
        solutions.add(i)
    return False


if __name__ == "__main__":
    num_list = [10, 15, 3, 7]
    ksum = 17
    print(solution(num_list, ksum))