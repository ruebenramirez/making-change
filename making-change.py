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

DEBUG = False


class Change:
    def __init__(self):
        self.coins = {}

    def add_coins(self, coin: int, count: int):
        self.coins.update({coin: count})

    def coins(self):
        return self.coins


def optimal_coinset(total: int, coinset: list):
    '''Create an optimal coinset list.

    Only use coins we're able to make change with.
    Remove duplicate coins.
    Sort the resulting optimal coinset list in reverse order to make it prep for efficient change calculation.'''
    optimal_coinset = []

    for coin in coinset:
        if coin <= total:
            if not coin in optimal_coinset:
                optimal_coinset.append(coin)

    optimal_coinset.sort(reverse=True)

    if optimal_coinset is None:
        raise Exception(f"Unable to make change. `optimal_coinset` built: {optimal_coinset}")

    if DEBUG: print(f"optimal_coinset list: {optimal_coinset}")
    return optimal_coinset


def make_change(total: int, coinset: list):
    '''return the optimal amount of change'''
    change = Change()

    for coin in optimal_coinset(total, coinset):
        if DEBUG: print(f"coin: {coin}")
        number_of_this_coin = total // coin
        if DEBUG: print(f"number of this coin to use: {number_of_this_coin}")
        change.add_coins(coin, number_of_this_coin)

        # calculate remaining total to make change for
        total = total - (coin * number_of_this_coin)
        if DEBUG: print(f"remaining total to make change for: {total}")


    return change.coins


if __name__ == "__main__":
    print(make_change(6, [1, 5, 10, 25]))
    print()
    print(make_change(6, [3, 4]))
    print()
    print(make_change(6, [1, 3, 4]))
    print()
    print(make_change(6, [5, 7]))
