"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cache_container = {}

    def wrapper(*args):
        if args in cache_container:
            print("returning cached result")
            return cache_container[args]
        else:
            result = func(*args)
            print("new input...caching result")
            cache_container[args] = result
            return result

    return wrapper
