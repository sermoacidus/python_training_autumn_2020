"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
import random
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    flag = 0
    with open(file_name) as f:
        for line in f:
            if not flag:
                _max, _min = int(line), int(line)
                flag = 1
            if int(line) > _max:
                _max = int(line)
            if int(line) <= _min:
                _min = int(line)
    return _min, _max


def create_tempfile():
    with open("testfile.txt", "w") as f:
        for i in range(0, random.randint(1, 100)):
            f.write(f"{random.randint(-1000000, 1000000)}\n")
