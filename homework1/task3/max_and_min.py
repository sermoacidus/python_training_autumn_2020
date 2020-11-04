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
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as f:
        file_generator = iter(f.readline, "")
        first_line = int(next(file_generator))
        min_, max_ = first_line, first_line
        try:
            while True:
                new_line = int(next(file_generator))
                if new_line > max_:
                    max_ = new_line
                elif new_line < min_:
                    min_ = new_line
        except StopIteration:
            pass
    return min_, max_
