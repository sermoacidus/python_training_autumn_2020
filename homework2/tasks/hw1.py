"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from string import printable, punctuation
from typing import List

filepath = "data.txt"


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "rb") as f:
        text = f.read()
        pattern_of_line_break = bytes("-\r\n", encoding="utf8")
        text_without_line_breaks = text.replace(pattern_of_line_break, b"")
        text_without_escape_ch = text_without_line_breaks.decode("unicode-escape")
        punctuation_set = punctuation + "»" + "«"
        for punct_symb in punctuation_set:
            text_without_escape_ch = text_without_escape_ch.replace(punct_symb, " ")
        words = text_without_escape_ch.split()
        for word in words:
            word.strip()
        return sorted(words, key=lambda x: len(set(x)), reverse=True)[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "rb") as f:
        counter = {}
        text = f.read().decode("unicode-escape")
        for symb in text:
            if symb in counter:
                counter[symb] += 1
            else:
                counter[symb] = 1
        return list(sorted(counter.items(), key=lambda item: item[1]))[0][0]


def count_punctuation_chars(file_path: str) -> int:
    punctuation_set = punctuation + "»" + "«"
    counter = 0
    with open(file_path, "rb") as f:
        text = f.read().decode("unicode-escape")
        for symb in text:
            if symb in punctuation_set:
                counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    with open(file_path, "rb") as f:
        text = f.read().decode("unicode-escape")
        for symb in text:
            if symb not in printable:
                counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "rb") as f:
        counter = {}
        text = f.read().decode("unicode-escape")
        for symb in text:
            if symb not in printable:
                if symb in counter:
                    counter[symb] += 1
                else:
                    counter[symb] = 1
        return list(sorted(counter.items(), key=lambda item: item[1], reverse=True))[0][
            0
        ]
