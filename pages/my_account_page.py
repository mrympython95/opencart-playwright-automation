from playwright.sync_api import Page

class MyAccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.my_account_heading = page.locator('h2:has-text("My Account")')
        self.link_logout = page.get_by_role("link", name="Logout")

    def click_logout(self):
        self.link_logout.click()