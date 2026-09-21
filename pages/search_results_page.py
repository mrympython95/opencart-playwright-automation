from playwright.sync_api import Page

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_page_header = page.locator("#content h1", has_text="Search -")
        self.search_products = page.locator("h4 > a")

    def select_product(self, product_name: str):
        self.search_products.get_by_text(
            product_name,
            exact=True
        ).click()