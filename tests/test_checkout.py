from playwright.sync_api import expect

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from utils.config import Config

def test_checkout_start(login_page):
    login_page.login(
        Config.TEST_USER_EMAIL, Config.TEST_USER_PASSWORD
    )

    home_page = HomePage(login_page.page)

    home_page.enter_product_name("iPhone")
    home_page.click_search()

    search_page = SearchResultsPage(home_page.page)
    search_page.select_product("iPhone")

    product_page = ProductPage(home_page.page)
    expect(product_page.product_name).to_have_text("iPhone")
    product_page.click_add_to_cart()
    expect(product_page.cnf_msg).to_contain_text("Success: You have added iPhone to your shopping cart!")

    product_page.click_items()
    product_page.click_view_cart()

    shopping_cart_page = ShoppingCartPage(home_page.page)
    expect(shopping_cart_page.product_name).to_have_text("iPhone")
    # Checkout


    shopping_cart_page.click_checkout()

    checkout_page = CheckoutPage(home_page.page)

    expect(
        checkout_page.page.locator("#content h1")
    ).to_have_text("Checkout")

    # Step 2: Billing Details
    checkout_page.click_continue()

    # Note: OpenCart demo has a JS race condition where Step 3's panel
    # sometimes stays collapsed after clicking Continue. We wait for
    # network to settle and manually expand it if needed.
    home_page.page.wait_for_load_state("networkidle")
    step3_header = home_page.page.locator("a[href='#collapse-shipping-address']")
    if not checkout_page.btn_continue_delivery_address.is_visible():
        step3_header.click()

    expect(checkout_page.btn_continue_delivery_address).to_be_visible(timeout=10000)
    checkout_page.click_continue_delivery_address()

    checkout_page.click_continue_shipping_method()
    checkout_page.check_terms()
    checkout_page.click_continue_payment_method()
    checkout_page.click_confirm_order()



