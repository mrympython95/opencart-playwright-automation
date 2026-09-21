
from playwright.sync_api import Page,expect

from pages.product_page import ProductPage
from pages.search_results_page import SearchResultsPage

def test_add_product_to_cart(home_page):
    home_page.enter_product_name("iPhone")
    home_page.click_search()

    search_page = SearchResultsPage(home_page.page)
    search_page.select_product("iPhone")

    product_page = ProductPage(home_page.page)
    expect(product_page.product_name).to_have_text("iPhone")
    # product_page.select_color("Blue")
    # product_page.set_quantity("5")
    product_page.click_add_to_cart()
    expect(product_page.cnf_msg).to_contain_text("Success: You have added iPhone to your shopping cart!")
