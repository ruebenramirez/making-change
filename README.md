
# Instructions - Making Change

Given a number "x" and a sorted array of coins "coinset", write a function
that returns the amounts for each coin in the coinset that sums up to X or
indicate an error if there is no way to make change for that x with the given
coinset. For example, with x=7 and a coinset of [1,5,10,25], a valid answer
would be {1: 7} or {1: 2, 5: 1}. With x = 3 and a coinset of [2,4] it should
indicate an error. Bonus points for optimality.

Use the following examples to test it out
A. x = 6 coinset = [1,5,10,25]
B. x = 6, coinset = [3,4]
C. x = 6, coinset = [1,3,4]
D. x = 6, coinset = [5,7]

# TODOs

- TODO: update code to return the fewest coins


# example run
note: the exception is expected since we're unable to make change for 6 with a coinset of [5, 7]
```
*[master][~/code/making-change]$ make run
poetry run python3 making_change.py
{1: 6}

{3: 2}

{1: 6}

Traceback (most recent call last):
  File "/home/rramirez/code/making-change/making_change.py", line 61, in <module>
    print(make_change(6, [5, 7]))
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/rramirez/code/making-change/making_change.py", line 49, in make_change
    raise CannotMakeChangeException(f"Unable to make change")
CannotMakeChangeException: Unable to make change
make: *** [Makefile:3: run] Error 1
```


# example test run

```
[master][~/code/making-change]$ make test
poetry run pytest .
=============================================================================== test session starts ===============================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0+repack
rootdir: /home/rramirez/code/making-change
collected 1 item

test_making_change.py .                                                                                                                                                     [100%]

================================================================================ 1 passed in 0.01s ================================================================================
```
