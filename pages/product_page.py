from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator("#content h1")
        self.dropdown_color = page.locator("#input-option226")
        self.txt_quantity = page.locator("#input-quantity")
        self.btn_add_to_cart =  page.locator("#button-cart")
        self.cnf_msg = page.locator(".alert.alert-success.alert-dismissible")
        self.btn_items = page.locator("#cart")
        self.link_view_cart = page.locator("#cart a").filter(
            has_text="View Cart"
        )

    def select_color(self, color: str):
        self.dropdown_color.select_option(label=color)

    def set_quantity(self, qty: str):
        self.txt_quantity.fill(qty)

    def click_add_to_cart(self):
        self.btn_add_to_cart.click()

    def click_items(self):
        self.btn_items.click()

    def click_view_cart(self):
        self.link_view_cart.click()
