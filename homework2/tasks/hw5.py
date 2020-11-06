"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(iterable, *args) -> list:
    if len(args) == 1:
        stop_index = [ind for ind, elem in enumerate(iterable) if elem == args[0]]
        return [elem for ind, elem in enumerate(iterable) if ind < stop_index[0]]
    start_index, stop_index = [
        ind for ind, elem in enumerate(iterable) if elem == args[0] or elem == args[1]
    ]
    if len(args) == 2:
        return [
            elem for ind, elem in enumerate(iterable) if start_index <= ind < stop_index
        ]
    if len(args) == 3:
        if args[2] > 0:
            result = [
                elem
                for ind, elem in enumerate(iterable)
                if start_index <= ind < stop_index
            ]
            return [elem for ind, elem in enumerate(result) if ind % args[2] == 0]
        if args[2] < 0:
            start_index, stop_index = [
                ind
                for ind, elem in enumerate(reversed(iterable))
                if (elem == args[0] or elem == args[1])
            ]
            result = [
                elem
                for ind, elem in (enumerate(reversed(iterable)))
                if start_index <= ind < stop_index
            ]
            return [elem for ind, elem in enumerate(result) if ind % args[2] == 0]
