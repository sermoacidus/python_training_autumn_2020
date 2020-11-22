import os

import pytest
from tasks_hw4.task1_read_file import read_magic_number


@pytest.fixture
def file_name(tmpdir, request):
    temp_file = tmpdir.join("test.txt")
    temp_file_name = os.path.join(temp_file.dirname, temp_file.basename)
    action_map = {"right": "2.9", "wrong": "3", "err": "a"}
    with open(temp_file_name, "w") as fh:
        for action, data in action_map.items():
            if request.param == action:
                fh.write(data + "\n")
    yield temp_file_name
    os.remove(temp_file_name)


@pytest.mark.parametrize("file_name", ["right"], indirect=["file_name"])
def test_different_values(file_name):
    assert read_magic_number(file_name) is True


@pytest.mark.parametrize("file_name", ["wrong"], indirect=["file_name"])
def test_different_values(file_name):
    assert read_magic_number(file_name) is False


@pytest.mark.parametrize("file_name", ["err"], indirect=["file_name"])
def test_different_values(file_name):
    with pytest.raises(ValueError, match="Wrong input.Digits in first line expected"):
        read_magic_number(file_name)
