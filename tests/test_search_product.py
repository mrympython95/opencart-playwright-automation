
from playwright.sync_api import Page,expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage

def test_search_product(home_page):

    home_page.enter_product_name(product_name="Canon EOS 5D")
    home_page.click_search()

    search_page = SearchResultsPage(home_page.page)

    expect(search_page.search_page_header).to_have_text("Search - Canon EOS 5D")
    search_page.select_product(product_name="Canon EOS 5D")
    product_page = ProductPage(home_page.page)
    expect(product_page.product_name).to_have_text("Canon EOS 5D")
