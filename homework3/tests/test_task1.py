from unittest.mock import MagicMock

from tasks_hw3.task1 import cache


@cache(times=3)
def some_func(a, b, name=None):
    return (a ** b) ** 2, name


def test_cache():

    test1 = some_func(100, 200, name="keywordarg")
    test2 = some_func(100, 200, name="keywordarg")
    test3 = some_func(100, 200, name="keywordarg")
    test4 = some_func(100, 200, name="keywordarg")
    test5 = some_func(100, 200, name="keywordarg")
    test6 = some_func(100, 200, name="keywordarg")
    assert test1 == test2 == test3 == test4 == test5 == test6
    assert test1 is test2, "first output is not cached"
    assert test2 is test3, "second output is not cached"
    assert test3 is test4, "third output is not cached"
    assert test4 is not test5, "output is cached, but must create new object"
    assert test5 is test6, "first output of new input is not cached"


def test_cache_with_mock():
    mock = MagicMock()
    func = cache(times=4)(mock)
    func(100, 200, name="keywordarg")
    func(100, 200, name="keywordarg")
    func(100, 200, name="keywordarg")
    func(100, 200, name="keywordarg")
    func(100, 200, name="keywordarg")
    func(100, 200, name="keywordarg")
    assert len(mock.mock_calls) == 2
