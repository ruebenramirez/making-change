# Making Change

# Given a number "x" and a sorted array of coins "coinset", write a function
# that returns the amounts for each coin in the coinset that sums up to X or
# indicate an error if there is no way to make change for that x with the given
# coinset. For example, with x=7 and a coinset of [1,5,10,25], a valid answer
# would be {1: 7} or {1: 2, 5: 1}. With x = 3 and a coinset of [2,4] it should
# indicate an error. Bonus points for optimality.

# Use the following examples to test it out
# A. x = 6 coinset = [1,5,10,25]
# B. x = 6, coinset = [3,4]
# C. x = 6, coinset = [1,3,4]
# D. x = 6, coinset = [5,7]

DEBUG = True


class Change:

    def __init__(self):
        self.coins = {}

    def add_coins(self, coin, count):
        self.coins.update({coin: count})

    def coins(self):
        return self.coin


def make_change(x, coinset):
    if DEBUG:
        print("making change for {x}".format(x=x))
        print("coinset: {cs}".format(cs=coinset))
    change = Change()
    for coin in coinset:
        if coin <= x:
            coin_count = x // coin
            if coin_count > 0:
                change.add_coins(coin, coin_count)
                x = x - (coin * coin_count)
        if x == 0:
            return change.coins

    raise Exception("Unable to make change: {change}".format(change=change))


print(make_change(6, [1, 5, 10, 25]))
print()
print(make_change(6, [3, 4]))
print()
print(make_change(6, [1, 3, 4]))
print()
print(make_change(6, [5, 7]))
