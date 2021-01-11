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


def optimal_coinset(target_change, coinset):
    """Only use coins we're able to make change with."""
    coins = []
    for coin in coinset:
        if coin <= target_change:
            coins.append(coin)
    return coins


def gen_change(change_target, coinset):
    """explore all possibilities to make target change given coins"""
    if change_target == 0:
        return []
    if change_target < 0:
        return None
    coinset = optimal_coinset(change_target, coinset)
    change = None
    for coin in coinset:
        change_remainder = change_target - coin
        change_option = gen_change(change_remainder, coinset)
        if change_option is not None:
            change_option.append(coin)
            if change is None or len(change_option) < len(change):
                change = change_option
    return change


def count_change(coins):
    """count change out into desired output format"""
    change = {}
    for coin in coins:
        count = change.get(coin, 0) + 1
        change[coin] = count
    return change


def make_change(x, coinset):
    try:
        coins = gen_change(x, coinset)
        return count_change(coins)
    except Exception:
        print("Unable to make change for {x} with these coins: {cs}".format(
            x=x, cs=coinset))
        return {}


print(make_change(6, [1, 5, 10, 25]))
print(make_change(6, [3, 4]))
print(make_change(6, [1, 3, 4]))
print(make_change(6, [5, 7]))
