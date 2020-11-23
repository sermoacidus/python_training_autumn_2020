import functools


def save_metainf_deco(source_func):
    def inner(func):
        def wrapper2(*args, **kwargs):
            wrapper2.__name__ = source_func.__name__
            wrapper2.__doc__ = source_func.__doc__
            wrapper2.__original_func = source_func
            result = func(*args, **kwargs)
            return result

        return wrapper2

    return inner


def print_result(func):
    @save_metainf_deco(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


if __name__ == "__main__":
    custom_sum([1, 2, 3], [4, 5])
    custom_sum(1, 2, 3, 4)

    print(custom_sum.__doc__)
    print(custom_sum.__name__)
    without_print = custom_sum.__original_func

    # the result returns without printing
    without_print(1, 2, 3, 4)
