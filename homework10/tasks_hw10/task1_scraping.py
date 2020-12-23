import asyncio
import json
import re
from itertools import islice

import aiohttp
import requests
import xmltodict
from bs4 import BeautifulSoup

"""
structure of 'enterprise_info' dictionary:
{company name: [year-uplift, company_URL, short_name, current_value, PE ratio, lowest_year_value, highest_year_val]}
"""
enterprise_info = {}
failed_to_parse = set()

URL = "https://markets.businessinsider.com"


def exchange_rate_parse():
    """
    Fetching USD/RUB exchange ratio
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    data = xmltodict.parse(response.content)
    for items in data["ValCurs"]["Valute"]:
        if items["Name"] == "Доллар США":
            return float(items["Value"].replace(",", "."))


exchange_ratio_USD_RUB = exchange_rate_parse()


def collect_names_and_year_profit(url: str):
    """
    saving companies' names, personal urls and their year profits
    into 'enterprise_info' dict {name:[year_profit,company_url]}
    """
    r = requests.get(url)
    soup = (
        BeautifulSoup(r.content, "html.parser")
        .find(class_="table table-small")
        .children
    )
    for ind, child in enumerate(soup):
        if ind > 2 and not isinstance(child, str):
            company_name = child.contents[1].text.lstrip()
            profit_indicator = float(
                child.contents[19].text.split()[1].replace(",", "")[:-1]
            )
            for link in child.find_all("a"):
                company_page = link.get("href")
                enterprise_info[company_name] = [profit_indicator, company_page]


async def parse_enterprise_url(url, entepr_name):
    """
    asynchronously fetching info from companies' URLS:
    short_name, current_value, PE ratio, 52weeks_low_value, 52weeks_high_value.
    then adding it to 'enterprise_info' dict
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            try:
                soup = BeautifulSoup(html, "html.parser")
                short_company_name = soup.find(
                    class_="price-section__category"
                ).text.split(" , ")[1]
                current_company_value = float(
                    soup.find(class_="price-section__current-value").text.replace(
                        ",", ""
                    )
                )
                company_p_e_ratio = float(
                    soup.find(class_="snapshot")
                    .contents[17]
                    .text.split()[0]
                    .replace(",", "")
                )
                company_52weeks_low = float(
                    re.findall("low52weeks: (.+),", str(soup.find_all("script")))[
                        0
                    ].replace(",", "")
                )
                company_52weeks_high = float(
                    re.findall("high52weeks: (.+),", str(soup.find_all("script")))[
                        0
                    ].replace(",", "")
                )
                enterprise_info[entepr_name].extend(
                    [
                        short_company_name,
                        current_company_value,
                        company_p_e_ratio,
                        company_52weeks_low,
                        company_52weeks_high,
                    ]
                )
            except:
                failed_to_parse.add(entepr_name)


def create_json_file(
    file_name: str, sorting_func, name_of_stat, formula_for_stat, reverse=False
):
    """
    creating json based on sorted 'enterprise_info' dict. Sorting functions taken from top10_*** functions
    """
    data = []
    sorted_companies_data = {
        key: enterprise_info[key]
        for key in sorted(
            enterprise_info,
            key=lambda x: sorting_func(enterprise_info, x),
            reverse=reverse,
        )
    }
    top10 = dict(islice(sorted_companies_data.items(), 10))
    for company, company_stats in top10.items():
        data.append(
            {
                "code": company_stats[2],
                "name": company,
                name_of_stat: formula_for_stat(company_stats),
            }
        )
    with open(file_name, "w") as fh:
        fh.write(json.dumps(data, indent=4))


def top10_lowest_PE():
    sorting_func = lambda x, y: x[y][4]
    name_of_stat_for_json = "P/E"
    get_PE_stat = lambda x: x[4]
    create_json_file(
        "top10_lowest_PE.json", sorting_func, name_of_stat_for_json, get_PE_stat
    )


def top10_expensive():
    sorting_func = lambda x, y: x[y][3]
    name_of_stat_for_json = "price"
    get_price_stat = lambda x: round(x[3] * exchange_ratio_USD_RUB, 2)
    create_json_file(
        "top10_expensive.json",
        sorting_func,
        name_of_stat_for_json,
        get_price_stat,
        reverse=True,
    )


def top10_year_uplift():
    sorting_func = lambda x, y: x[y][0]
    name_of_stat_for_json = "growth"
    get_growth_stat = lambda x: x[0]
    create_json_file(
        "top10_growth.json",
        sorting_func,
        name_of_stat_for_json,
        get_growth_stat,
        reverse=True,
    )


def top10_profit_buy_year_lowest_sell_year_highest():
    sorting_func = lambda x, y: 100 * x[y][6] / x[y][5] - 100
    name_of_stat_for_json = "potential profit"
    get_potent_profit_stat = lambda x: round(100 * x[6] / x[5] - 100, 2)
    create_json_file(
        "top10_profit_buy_year_lowest_sell_year_highest.json",
        sorting_func,
        name_of_stat_for_json,
        get_potent_profit_stat,
        reverse=True,
    )


async def parse_enterprises_urls():
    tasks = [
        asyncio.create_task(
            parse_enterprise_url(f"https://markets.businessinsider.com{stat[1]}", name)
        )
        for name, stat in enterprise_info.items()
    ]
    await asyncio.gather(*tasks)


def main():
    pagination_page_index = 1
    while True:
        pagination_page_url = (
            f"{URL}/index/components/s&p_500?p={pagination_page_index}"
        )
        pagination_page_index += 1
        try:
            collect_names_and_year_profit(pagination_page_url)
        except AttributeError:  # 'No pagination pages left, starting to parse'
            break
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parse_enterprises_urls())
    for failed in failed_to_parse:
        del enterprise_info[failed]
    top10_expensive()
    top10_lowest_PE()
    top10_year_uplift()
    top10_profit_buy_year_lowest_sell_year_highest()


if __name__ == "__main__":
    main()
