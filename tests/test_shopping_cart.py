from playwright.sync_api import expect

from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.search_results_page import SearchResultsPage


def test_shopping_cart_page(home_page):
    home_page.enter_product_name("iPhone")
    home_page.click_search()

    search_page = SearchResultsPage(home_page.page)
    search_page.select_product("iPhone")

    product_page = ProductPage(home_page.page)

    expect(product_page.product_name).to_have_text("iPhone")

    # product_page.select_color("Blue")
    # product_page.set_quantity("5")

    product_page.click_add_to_cart()

    expect(product_page.cnf_msg).to_contain_text(
        "Success: You have added iPhone to your shopping cart!"
    )

    product_page.click_items()
    product_page.click_view_cart()

    shopping_cart_page = ShoppingCartPage(home_page.page)

    expect(shopping_cart_page.product_name).to_have_text("iPhone")

    # expect(shopping_cart_page.quantity).to_have_value("5")

    expect(
        shopping_cart_page.lbl_total_price
    ).to_have_text("$123.20")

    # shopping_cart_page.click_checkout()