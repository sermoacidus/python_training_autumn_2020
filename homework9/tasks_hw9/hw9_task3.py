"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
"""
from itertools import chain
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    extension_pattern = f"**/*.{file_extension}"
    files = list(dir_path.glob(extension_pattern))

    sum_of_elements = 0

    for file in files:
        with open(file, "r") as file_handler:
            if not tokenizer:
                sum_of_elements += sum(1 for _ in file_handler)
            else:
                sum_of_elements += sum(
                    1 for _ in chain.from_iterable(map(tokenizer, file_handler))
                )
    return sum_of_elements
