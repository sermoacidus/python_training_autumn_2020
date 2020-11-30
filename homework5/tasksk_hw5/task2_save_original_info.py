import functools


def save_metainf_deco(source_func):
    def inner(func):
        def deco_wrapper(*args, **kwargs):
            deco_wrapper.__name__ = source_func.__name__
            deco_wrapper.__doc__ = source_func.__doc__
            deco_wrapper.__original_func = source_func
            result = func(*args, **kwargs)
            return result

        return deco_wrapper

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
