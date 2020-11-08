from tasks.hw4 import cache


def func(a, b):
    return (a ** b) ** 2


def test_cache():
    testfunc = cache(func)
    test1 = testfunc(100, 200)
    test2 = testfunc(100, 200)
    assert test1 is test2
