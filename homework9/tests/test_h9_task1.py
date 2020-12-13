import os

import pytest
from tasks_hw9.hw9_task1_ import merge_sorted_files

test_data = [["2\n", "5\n", "9\n"], ["1\n", "6\n", "9\n"], ["5\n", "7\n", "10\n"]]


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
    yield file_names
    for name in file_names:
        os.remove(name)


def test_getting_iterator(name_of_test_file):
    assert list(merge_sorted_files(name_of_test_file)) == [1, 2, 5, 5, 6, 7, 9, 9, 10]
