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
        def inner_f(*args, **kwargs):
            immut_args = (args, str(kwargs)).__hash__()
            if immut_args in cache_container and cache_container[immut_args][1] > 0:
                output = cache_container[immut_args][0]
                cache_container[immut_args][1] -= 1
                if cache_container[immut_args][1] == 0:
                    del cache_container[immut_args]

                return output
            else:
                result = func(*args, **kwargs)
                cache_container[immut_args] = [result, times]

            return result

        return inner_f

    return wrapper
