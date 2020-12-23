from collections import OrderedDict
from unittest.mock import MagicMock

import requests
import tasks_hw10.task1_scraping as task


def test_exchange_rate_func(monkeypatch):
    test_xml = OrderedDict(
        [
            (
                "ValCurs",
                OrderedDict(
                    [
                        ("x", "x"),
                        (
                            "Valute",
                            [
                                OrderedDict(
                                    [
                                        ("x", "x"),
                                        ("Name", "Доллар США"),
                                        ("Value", "56,9042"),
                                    ]
                                )
                            ],
                        ),
                    ]
                ),
            )
        ]
    )
    monkeypatch.setattr(
        requests, "get", MagicMock(return_value=requests.models.Response)
    )
    monkeypatch.setattr(
        requests.models.Response, "content", MagicMock(return_value=None)
    )
    monkeypatch.setattr(task.xmltodict, "parse", MagicMock(return_value=test_xml))
    assert task.exchange_rate_parse() == 56.9042


def test_collect_names_and_year_profit_func(monkeypatch):
    with open("test_index_1.html", "rb") as fh:
        test_file = fh.read()

        class MockResponse:
            content = test_file

        def mock_get(*args, **kwargs):
            return MockResponse()

        monkeypatch.setattr(requests, "get", mock_get)
        task.collect_names_and_year_profit("url")
        assert task.enterprise_info["3M "] == [3.22, "/stocks/mmm-stock"]
