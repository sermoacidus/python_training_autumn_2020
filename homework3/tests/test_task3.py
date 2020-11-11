import pytest
from tasks_hw3 import task3


def test_class_functions():
    positive_even = task3.Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(100)) == [i for i in range(2, 100) if i % 2 == 0]


@pytest.fixture
def define_sample_data():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    return sample_data


def test_make_filter(define_sample_data):
    assert task3.make_filter(name="polly", type="bird").apply(define_sample_data) == [
        define_sample_data[1]
    ]
