from pathlib import Path

import pytest
import tasks.hw1


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        (
            (Path("tests/part for test.txt")),
            [
                "Gefährdung",
                "handelt",
                "Kernfrage",
                "bringt",
                "unserer",
                "heißt",
                "Frage",
                "sich",
                "Zeit",
                "Fälle",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(input_, expected_result):
    actual_result = tasks.hw1.get_longest_diverse_words(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        ((Path("tests/part for test.txt")), "E"),
    ],
)
def test_get_rarest_char(input_, expected_result):
    actual_result = tasks.hw1.get_rarest_char(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        ((Path("tests/part for test.txt")), 4),
    ],
)
def test_count_punctuation_chars(input_, expected_result):
    actual_result = tasks.hw1.count_punctuation_chars(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        ((Path("tests/part for test.txt")), 3),
    ],
)
def test_count_non_ascii_chars(input_, expected_result):
    actual_result = tasks.hw1.count_non_ascii_chars(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        ((Path("tests/part for test.txt")), "ä"),
    ],
)
def test_get_most_common_non_ascii_char(input_, expected_result):
    actual_result = tasks.hw1.get_most_common_non_ascii_char(input_)
    assert actual_result == expected_result
