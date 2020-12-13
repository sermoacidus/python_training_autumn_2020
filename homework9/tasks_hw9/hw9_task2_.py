"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager


class Supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self.exception:
            return self


@contextmanager
def supressor_func(exception):
    try:
        yield
    except exception:
        pass
