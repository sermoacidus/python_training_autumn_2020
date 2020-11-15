"""
Write a function that will receive a string and write it to stderr
if line starts with "error" and to the stdout otherwise.
"""
import sys


def my_precious_logger(text: str):
    print(text, file=sys.stderr) if text.startswith("error") else print(text)
