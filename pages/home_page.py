from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.link_my_account = page.locator("span:has-text('My Account')")
        self.link_register = page.locator("a:has-text('Register')")
        self.link_login = page.locator("a:has-text('Login')")
        self.txt_search_box = page.get_by_placeholder("Search")
        self.btn_search = page.locator("button.btn.btn-default.btn-lg")

    def click_my_account(self):
        self.link_my_account.click()

    def click_register(self):
        self.link_register.click()

    def click_login(self):
        self.link_login.click()

    def enter_product_name(self, product_name):
        self.txt_search_box.fill(product_name)

    def click_search(self):
        self.btn_search.click()