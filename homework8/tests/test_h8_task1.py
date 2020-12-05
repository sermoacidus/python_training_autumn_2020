import os

import pytest
from tasks_hw8.hw8_task1 import CustomStorageReader

sample = """name=kek
last_name=top
song_name=shadilay
power=9001"""


@pytest.fixture
def name_of_test_file(tmpdir):
    temp_file = tmpdir.join("test.txt")
    temp_file_name = os.path.join(temp_file.dirname, temp_file.basename)
    with open(temp_file_name, "w") as fh:
        fh.write(sample)
    yield temp_file_name
    os.remove(temp_file_name)


def test_reading_values(name_of_test_file):
    storage = CustomStorageReader(name_of_test_file)
    assert storage["name"] == "kek"
    assert storage.last_name == "top"


def test_setting_values(name_of_test_file):
    storage = CustomStorageReader(name_of_test_file)
    storage["test1"] = "test1"
    storage.test2 = "test2"
    assert storage.test1 == "test1"
    assert storage["test2"] == "test2"


def test_exception_if_key_is_present(name_of_test_file):
    storage = CustomStorageReader(name_of_test_file)
    with pytest.raises(
        ValueError,
        match='The key "power" is already present is storage. Its value is "9001"',
    ):
        storage.power = "test"


def test_if_value_is_converted_to_int(name_of_test_file):
    storage = CustomStorageReader(name_of_test_file)
    assert isinstance(storage.power, int)
