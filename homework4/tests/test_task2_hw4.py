from unittest.mock import MagicMock

import pytest
import tasks_hw4.task2_mock


def test_connection():
    mock = MagicMock(return_value=".....")
    tasks_hw4.task2_mock.connect_to_web = mock

    assert tasks_hw4.task2_mock.count_dots_on_i("whatever.com") == 5
    assert mock.mock_calls


def test_failed_connection():
    mock = MagicMock(side_effect=ValueError("Unreachable whatever.com"))
    tasks_hw4.task2_mock.connect_to_web = mock

    with pytest.raises(ValueError, match=("Unreachable whatever.com")):
        tasks_hw4.task2_mock.count_dots_on_i("whatever.com")
    assert mock.mock_calls


def test_coonect_to_web_not_mock(capsys):
    print(tasks_hw4.task2_mock.connect_to_web("https://www.google.com/")[0:11])
    captured = capsys.readouterr()
    assert captured.out == "GoogleПоиск\n"
