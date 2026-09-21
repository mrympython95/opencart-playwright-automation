import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def home_page(page: Page) -> HomePage:
    page.goto("index.php")
    return HomePage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    page.goto("index.php?route=account/login")
    return LoginPage(page)