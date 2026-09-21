from playwright.sync_api import Page
from pages.my_account_page import MyAccountPage
from utils.config import Config


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.txt_email_address = page.locator("#input-email")
        self.txt_password = page.locator("#input-password")
        self.login_button = page.locator("input[value='Login']")
        self.txt_error_message = page.locator(".alert.alert-danger.alert-dismissible")

    def set_email(self, email: str):
        self.txt_email_address.fill(email)

    def set_password(self, password: str):
        self.txt_password.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

