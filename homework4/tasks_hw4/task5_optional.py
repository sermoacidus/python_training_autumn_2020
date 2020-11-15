"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs
"""


def fizzbuzz(n: int):
    """

    >>> list(fizzbuzz(5))
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    fizzes = ["n", "n", "f"] * n
    buzzes = ["n", "n", "n", "n", "b"] * n
    temp_res = list(map(lambda x: x[0] + x[1], list(zip(fizzes, buzzes))))

    seq = "_".join(temp_res)
    seq = seq.replace("fn", "f")
    seq = seq.replace("nb", "b")
    seq = seq.replace("fb", "o")
    seq = seq.replace("nn", "N")
    seq = seq.replace("_", "")
    result = ""
    for i in range(len(seq)):
        result = result + seq[i].replace("N", str(i + 1) + ",")
    result = result.replace("f", "Fizz,")
    result = result.replace("b", "Buzz,")
    result = result.replace("o", "FizzBuzz,")
    str_to_list = result.split(",")
    for elem in str_to_list[:n]:
        yield str(elem)
