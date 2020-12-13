"""
Write a function that merges integer from sorted files and returns an iterator
"""

from pathlib import Path
from typing import Iterator, List, Union


def file_opener(filename) -> Iterator:
    with open(filename, "r") as fh:
        while True:
            new_line = fh.readline().rstrip()
            if not new_line.isdigit():
                break
            yield int(new_line)


def check_values_left(iterators: list):
    for iterator in iterators:
        if iterator[1] is None:
            try:
                iterator[1] = next(iterator[0])
                break
            except StopIteration:
                iterator[1] = 0
                iterator.append("Used")


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    iterators = []
    for file in file_list:
        iterator = iter(file_opener(file))
        iterators.append([iterator, next(iterator)])
    while iterators:
        for item in iterators:
            if len(item) > 2:
                iterators.remove(item)
        for item in sorted(iterators, key=lambda x: x[1]):
            if len(item) > 2:
                continue
            yield item[1]
            item[1] = None
            check_values_left(iterators)
            break
