

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
