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
                max_num, min_num = int(line), int(line)
                flag = 1
            if int(line) > max_num:
                max_num = int(line)
            if int(line) <= min_num:
                min_num = int(line)
    return min_num, max_num
