from playwright.sync_api import Page


class SuccessPage:
    def __init__(self, page: Page):
        self.page = page
        self.success_message = page.locator("#content h1")
        self.btn_continue = page.get_by_role("link", name="Continue")

    def click_continue(self):
        self.btn_continue.click()