"""
Basic Test Example for Pytest + Selenium Webdriver
"""

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "panda"

    # Given That results are displayed for "panda"
    search_page.load()

    # When user searches for "panda"
    search_page.search(PHRASE)

    # Then the result title contains "panda"
    assert PHRASE in result_page.title()

    # AND the search query contains "panda"
    assert PHRASE == result_page.search_input_values()

    # AND the search result contains "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    raise Exception("Incomplete Test")
