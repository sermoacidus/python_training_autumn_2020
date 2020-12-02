"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

"""


def backspace_compare(first: str, second: str):
    """
    >>> backspace_compare('a##c','#a#c')
    True
    >>> backspace_compare('ab#c','ad#c')
    True
    >>> backspace_compare('a#c','b')
    False
    >>> backspace_compare('a####c', 'a##c')
    True
    """
    data = {first: [], second: []}
    for origin, modification in data.items():
        for letter in origin:
            if letter != "#":
                modification.append(letter)
            elif modification:
                modification.pop()
    return data[first] == data[second]
