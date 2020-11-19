from urllib.request import urlopen

from bs4 import BeautifulSoup


def connect_to_web(url: str):
    try:
        with urlopen(url) as f:
            html_page = f.read().decode("utf-8")
            soup = BeautifulSoup(html_page, "lxml")
            return soup.text
    except ValueError:
        print(f"Unreachable {url}")


def count_dots_on_i(url: str) -> int:
    amount_of_dots = 0
    text = connect_to_web(url)
    for symb in text:
        if symb == ".":
            amount_of_dots += 1
    return amount_of_dots
