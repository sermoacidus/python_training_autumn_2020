from tasks_hw3.task1 import cache


def some_func(a, b):
    return (a ** b) ** 2


def test_cache():
    test_func = cache(times=3)(some_func)
    test1 = test_func(100, 200)
    test2 = test_func(100, 200)
    test3 = test_func(100, 200)
    test4 = test_func(100, 200)
    test5 = test_func(100, 200)
    test6 = test_func(100, 200)
    assert test1 == test2 == test3 == test4 == test5 == test6
    assert test1 is test2
    assert test2 is test3
    assert test3 is test4
    assert test4 is not test5
    assert test5 is test6
