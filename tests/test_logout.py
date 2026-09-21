from playwright.sync_api import Page, expect
from pages.my_account_page import MyAccountPage
from pages.logout_page import LogoutPage
from utils.config import Config

def test_user_logout(login_page):
    login_page.login(
        Config.TEST_USER_EMAIL,
        Config.TEST_USER_PASSWORD,
    )
    my_account_page = MyAccountPage(login_page.page)
    expect(my_account_page.my_account_heading).to_be_visible()

    my_account_page.click_logout()
    logout_page = LogoutPage(login_page.page)
    expect(logout_page.btn_continue).to_be_visible()