from src.pages.Common import get_login_url


class LoginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(get_login_url())

    def provide_email_and_password(self, email, password):
        self.page.locator("input[name=\"email\"]").click()
        self.page.locator("input[name=\"email\"]").fill(email)
        self.page.locator("input[name=\"password\"]").click()
        self.page.locator("input[name=\"password\"]").fill(password)
        self.page.get_by_role("button", name="Prijavi se").click()
