import os
from pathlib import Path

import pytest
from tasks_hw9.hw9_task3 import universal_file_counter

test_data = [
    ["2\n", "5\n", "9 10\n"],
    ["1\n", "6\n", "9 15\n", "5\n"],
    ["5\n", "7\n", "10\n"],
]


@pytest.fixture
def name_of_test_file(tmpdir):
    file_names = []
    for ind, test_set in enumerate(test_data):
        temp_file = tmpdir.join(f"test{ind}.txt")
        temp_file_name = os.path.join(temp_file.dirname, temp_file.basename)
        file_names.append(temp_file_name)
        with open(temp_file_name, "w") as fh:
            for line in test_set:
                fh.write(line)
    yield Path(temp_file.dirname)
    for name in file_names:
        os.remove(name)


def test_count_without_tokenizer(name_of_test_file):
    assert universal_file_counter(name_of_test_file, "txt") == 10


def test_count_with_tokenizer(name_of_test_file):
    assert universal_file_counter(name_of_test_file, "txt", str.split) == 12
