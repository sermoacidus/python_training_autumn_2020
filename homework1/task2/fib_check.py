"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 2:
        return False
    elif len(data) == 2:
        if not (data[0] == 1 or data[0] == 0):
            return False
        elif not data[1] == 1:
            return False
        else:
            return True
    else:
        for ind, elem in enumerate(data):
            if ind >= 2:
                if elem == data[ind - 1] + data[ind - 2]:
                    continue
                else:
                    return False
        return True
