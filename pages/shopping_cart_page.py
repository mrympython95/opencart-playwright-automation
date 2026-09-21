from playwright.sync_api import Page

class ShoppingCartPage:
    def __init__(self, page: Page):
        self.page = page

        self.product_name = page.locator("#content td.text-left a")
        self.quantity = page.locator("input[name^='quantity']")

        self.lbl_total_price = page.locator(
            "tr", has_text="Total:"
        ).locator("td").last

        self.btn_checkout = page.get_by_role(
            "link", name="Checkout", exact=True
        )

    def click_checkout(self):
        self.btn_checkout.click()