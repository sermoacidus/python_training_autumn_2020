from tasks.hw4 import cache


def func(a, b):
    return (a ** b) ** 2


def test_cache():
    test1 = cache(func)
    test2 = cache(func)
    assert test1(100, 200) == test2(100, 200)
