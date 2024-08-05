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

class CannotMakeChangeException(Exception):
    pass

def used_this_coin_to_make_change(coin: int):
    return coin > 0

def coin_too_large(coin: int, total: int):
    return coin > total

def correct_change(change_made, correct_change):
    return change_made == correct_change

def make_change(total: int, coinset: list):
    while len(coinset) > 0:
        change_made_total = 0
        change = {}
        for coin in coinset:
            if coin_too_large(coin, total):
                break
            remaining_change_to_make = (total - change_made_total)
            coin_count = remaining_change_to_make // coin
            if used_this_coin_to_make_change(coin_count):
                change_made_total += (coin * coin_count)
                change.update({coin: coin_count})

        if not correct_change(change_made_total, total):
            # remove the coin we cannot use to make change with
            coinset.pop(0)
        else:
            # break out of the loop if we have the correct change
            return change

    raise CannotMakeChangeException(f"Unable to make change")

if __name__ == "__main__":
    print(make_change(6, [1, 5, 10, 25]))
    print()
    print(make_change(6, [3, 4]))
    print()
    print(make_change(6, [1, 3, 4]))
    print()
    print(make_change(6, [5, 7]))
