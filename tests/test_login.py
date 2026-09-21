from pathlib import Path

import pytest
from playwright.sync_api import expect

from pages.my_account_page import MyAccountPage
from utils.config import Config
from utils.data_reader_util import read_json_data


@pytest.mark.login
def test_login_with_invalid_credentials(login_page):
    login_page.login(
        "invalid@example.com",
        "WrongPassword123"
    )

    expect(
        login_page.txt_error_message
    ).to_be_visible()


def test_login_with_valid_credentials(login_page):
    login_page.login(
        Config.TEST_USER_EMAIL,
        Config.TEST_USER_PASSWORD
    )
    my_account_page = MyAccountPage(login_page.page)
    expect(my_account_page.my_account_heading).to_be_visible()