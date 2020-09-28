"""
 You have n fair coins and you flip them all at the same time.
 Any that come up tails you set aside.
 The ones that come up heads you flip again.
 How many rounds do you expect to play before only one coin remains?
 Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""
import random
print(random.randint(0, 1))


class Solution():
    def __init__(self, n):
        self.coins = n

    @staticmethod
    def toss_and_seperate_coins(coin_count):
        '''
        Toss function
        0: heads
        1: tails
        '''
        def toss_coin():
            return random.randint(0,1)

        iteration_count = 0
        while coin_count > 0:
            iteration_count += 1
            for coin in range(coin_count):
                res = toss_coin()
                if res == 1:
                    coin_count -= 1
        return  iteration_count

    def solve(self):
        print("Total number of given coins are : {} ".format(self.coins))
        rounds = self.toss_and_seperate_coins(self.coins)
        print("Total Number of rounds to be played before exhausting coins are : {} ".format(rounds))

s = Solution(10)
s.solve()