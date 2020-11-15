import os

import pytest
from tasks_hw4.task1_read_file import read_magic_number


@pytest.fixture
def create_files_with_legitimate_data():
    file_name = os.path.dirname(__file__) + "test_right_answers.txt"
    with open(file_name, "w") as file_handler:
        file_handler.write("2.9")
        return file_name


@pytest.fixture
def create_files_with_exceptions():
    file_name = os.path.dirname(__file__) + "test_exceptions_task1.txt"
    file_handler = open(file_name, "w")
    file_handler.write("a")
    yield file_name
    file_handler.close()
    os.remove(file_name)


def test_task_positive(create_files_with_legitimate_data):
    assert read_magic_number(create_files_with_legitimate_data)
    os.remove(create_files_with_legitimate_data)


def test_task_negative(create_files_with_exceptions):
    with pytest.raises(ValueError, match="WrongValue"):
        read_magic_number(create_files_with_exceptions)
