from pathlib import Path

from tasks_hw8.hw8_task2 import TableData

presidents = TableData(
    database_name=Path("tests/example.sqlite"), table_name="presidents"
)
books = TableData(database_name=Path("tests/example.sqlite"), table_name="books")


def test_length_method():
    assert len(presidents) == 3
    assert len(books) == 3


def test_get_item_method():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert books["1984"] == ("1984", "Orwell")


def test_contains_method():
    assert ("1984" in books) is True
    assert ("Lukashenko" in presidents) is False
    assert ("Trump" in presidents) is True


def test_iteration(capsys):
    for president in presidents:
        print(president["name"])
    captured = capsys.readouterr()
    assert captured.out == "Yeltsin\nTrump\nBig Man Tyrone\n"
    for book in books:
        print(book["author"])
    captured = capsys.readouterr()
    assert captured.out == "Bradbury\nHuxley\nOrwell\n"
