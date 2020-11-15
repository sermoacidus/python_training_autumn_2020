from urllib.request import urlopen


def connect_to_web(url: str):
    try:
        with urlopen(url) as f:
            return f.read()
    except ValueError:
        print(f"Unreachable {url}")


def count_dots_on_i(url: str) -> int:
    amount_of_dots = 0
    text = str(connect_to_web(url))
    for symb in text:
        if symb == ".":
            amount_of_dots += 1
    return amount_of_dots
