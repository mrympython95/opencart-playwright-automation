from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.btn_continue=  page.locator(".btn.btn-primary")

    def click_logout(self):
        self.btn_continue.click()