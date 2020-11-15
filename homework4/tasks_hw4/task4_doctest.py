"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
"""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    - Install Python 3.8 (https://www.python.org/downloads/)
    - Install pytest `pip install pytest`
    - Clone the repository https://github.com/sermoacidus/python_training_autumn_2020
    - Checkout branch master
    - Open terminal
    - "cd" to homework4/tasks4_hw4
    - to check a doc-test using pytest, write in console 'pytest --doctest-modules'
    - in case tests are not okey, you will see Failure message, otherwise you will see that the doctest is passed

    >>> fizzbuzz(20)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
    >>> fizzbuzz(0)
    []
    """
    sequence = list(range(1, n + 1))
    for ind, elem in enumerate(sequence):
        if (elem % 3) == 0 and (elem % 5) == 0:
            sequence[ind] = "FizzBuzz"
        elif elem % 3 == 0 and not elem % 5 == 0:
            sequence[ind] = "Fizz"
        elif not elem % 3 == 0 and elem % 5 == 0:
            sequence[ind] = "Buzz"
    return sequence
