import pytest
import tasks.hw1

MY_TEST_SET = "part for test.txt"
TASK_SET = "data.txt"


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        (
            (MY_TEST_SET),
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
        (
            (TASK_SET),
            [
                "Souveränitätsansprüche",
                "unmißverständliche",
                "Bevölkerungsabschub",
                "symbolischsakramentale",
                "Kollektivschuldiger",
                "unverhältnismäßig",
                "Werkstättenlandschaft",
                "Schicksalsfiguren",
                "Selbstverständlich",
                "Verwaltungsmaßnahme",
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
        (MY_TEST_SET, "E"),
        (TASK_SET, "›"),
    ],
)
def test_get_rarest_char(input_, expected_result):
    actual_result = tasks.hw1.get_rarest_char(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        (MY_TEST_SET, 4),
        (TASK_SET, 5391),
    ],
)
def test_count_punctuation_chars(input_, expected_result):
    actual_result = tasks.hw1.count_punctuation_chars(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        (MY_TEST_SET, 3),
        (TASK_SET, 2972),
    ],
)
def test_count_non_ascii_chars(input_, expected_result):
    actual_result = tasks.hw1.count_non_ascii_chars(input_)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["input_", "expected_result"],
    [
        (MY_TEST_SET, "ä"),
        (TASK_SET, "ä"),
    ],
)
def test_get_most_common_non_ascii_char(input_, expected_result):
    actual_result = tasks.hw1.get_most_common_non_ascii_char(input_)
    assert actual_result == expected_result
