import os

import pytest
from tasks_hw4.task1_read_file import read_magic_number


@pytest.fixture
def name_of_test_file(tmpdir):
    test_files = []

    def file_creator():
        temp_file = tmpdir.join("test.txt")
        temp_file_name = os.path.join(temp_file.dirname, temp_file.basename)
        test_files.append(temp_file_name)
        return temp_file_name

    def arg_courier(param=None):
        action_map = {"right": "2.9", "wrong": "3", "err": "a"}
        file_name = file_creator()
        with open(file_name, "w") as fh:
            for action, data in action_map.items():
                if param == action:
                    fh.write(data + "\n")
        return file_name

    yield arg_courier
    os.remove(test_files[0])


def test_different_values(name_of_test_file):
    assert read_magic_number(name_of_test_file(param="right")) is True
    assert read_magic_number(name_of_test_file(param="wrong")) is False
    with pytest.raises(ValueError, match="Wrong input.Digits in first line expected"):
        read_magic_number(name_of_test_file(param="err"))
