"""
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
"""


def cache(times):
    cache_container = {}

    def wrapper(func):
        def inner_f(*args):

            if args in cache_container and cache_container[args][1] > 0:
                output = cache_container[args][0]
                cache_container[args][1] -= 1
                if cache_container[args][1] == 0:
                    del cache_container[args]
                return output
            else:
                result = func(*args)
                cache_container[args] = [result, times]

            return result

        return inner_f

    return wrapper
