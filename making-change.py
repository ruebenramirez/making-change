import functools

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


@functools.lru_cache()
def optimal_coinset(x, coinset):
    """Only use coins we're able to make change with."""
    coinset = []
    for coin in coinset:
        if x <= coin:
            coinset.append(coin)
    return coinset


def make_change(x, coinset):
    if x == 0:
        return {}
    coinset = optimal_coinset(x, coinset)
    change = {}
    for coin in coinset:
        if coin <= x:
            coin_count = x // coin
            if coin_count > 0:
                change.update({coin: coin_count})
                x = x - (coin * coin_count)
        if x == 0:
            return change

    raise Exception("Unable to make change: {change}".format(change=change))


print(make_change(6, [1, 5, 10, 25]))
# print()
# print(make_change(6, [3, 4]))
# print()
# print(make_change(6, [1, 3, 4]))
# print()
# print(make_change(6, [5, 7]))
