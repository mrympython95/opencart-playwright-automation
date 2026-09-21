
from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.txt_first_name = page.get_by_placeholder("First Name")
        self.txt_last_name = page.get_by_placeholder("Last Name")
        self.txt_email = page.get_by_placeholder("E-Mail")
        self.txt_telephone = page.get_by_placeholder("Telephone")
        self.txt_password = page.get_by_placeholder(
            "Password",
            exact=True
        )
        self.txt_confirm_password = page.get_by_placeholder(
            "Password Confirm",
            exact=True
        )
        self.chk_policy = page.locator("input[value='1'][name='agree']")
        self.btn_continue = page.locator("input[value='Continue']")
        self.confirmation_message = page.locator("#content h1")

    def set_first_name(self, fname: str):
        self.txt_first_name.fill(fname)

    def set_last_name(self, lname: str):
        self.txt_last_name.fill(lname)

    def set_email(self, email: str):
        self.txt_email.fill(email)

    def set_telephone(self, tel: str):
        self.txt_telephone.fill(tel)

    def set_password(self, pw: str):
        self.txt_password.fill(pw)

    def set_confirm_password(self, pw: str):
        self.txt_confirm_password.fill(pw)

    def check_policy(self):
        self.chk_policy.check()

    def click_continue(self):
        self.btn_continue.click()

    # def complete_registration(self, user_data: dict):
    #     self.set_first_name("first name")
    #     self.set_last_name("last name")
    #     self.set_email("email")
    #     self.set_telephone("telephone")
    #     self.set_password("password")
    #     self.set_confirm_password("password")
    #     self.check_policy()
    #     self.click_continue()

