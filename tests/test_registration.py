import pytest
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage
from utils.random_data_util import RandomDataUtil

def test_user_registration(home_page):
    home_page.click_my_account()
    home_page.click_register()

    registration_page = RegistrationPage(home_page.page)
    random_data = RandomDataUtil()

    first_name =random_data.get_first_name()
    last_name =random_data.get_last_name()
    email = random_data.get_email()
    telephone = random_data.get_phone_number()
    password = random_data.get_password()

    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_telephone(telephone)
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)

    registration_page.check_policy()
    registration_page.click_continue()

    expect(registration_page.confirmation_message).to_have_text("Your Account Has Been Created!")



