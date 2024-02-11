from src.pages.Common import get_login_url
from src.pages.Common import get_reset_password_link


class Reset:
    def __init__(self, page):
        self.page = page

    def navigate_to_reset_password_page_from_login(self):
        self.page.goto(get_login_url())
        self.page.get_by_role("button", name="Zatraži novu lozinku").click()

    def navigate_to_reset_password_page(self):
        self.page.goto(get_reset_password_link())

    def request_new_password_for_user(self, email):
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill(email)
        self.page.get_by_role("button", name="Pošalji upute").click()
