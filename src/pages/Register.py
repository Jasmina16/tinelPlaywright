from src.pages.Common import get_register_url
from src.pages.Common import get_login_url


class RegisterPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_register_page(self):
        self.page.goto(get_register_url())

    def navigate_to_register_page_from_login_page(self):
        self.page.goto(get_login_url())
        self.page.get_by_role("button", name="Nemaš korisnički račun?").click()

    def enter_firstname(self, firstname):
        self.page.locator("input[name=\"firstName\"]").click()
        self.page.locator("input[name=\"firstName\"]").fill(firstname)

    def enter_lastname(self, lastname):
        self.page.locator("input[name=\"lastName\"]").click()
        self.page.locator("input[name=\"lastName\"]").fill(lastname)

    def enter_email(self, email):
        self.page.locator("input[name=\"email\"]").click()
        self.page.locator("input[name=\"email\"]").fill(email)

    def enter_password(self, password):
        self.page.get_by_label("Lozinka:").click()
        self.page.get_by_label("Lozinka:").fill(password)

    def confirm_password(self, confirm_pass):
        self.page.get_by_label("Unesi lozinku ponovo").click()
        self.page.get_by_label("Unesi lozinku ponovo").fill(confirm_pass)

    def enter_zip(self, zip):
        self.page.locator("input[name=\"zip\"]").click()
        self.page.locator("input[name=\"zip\"]").fill(zip)

    def enter_country(self, country):
        self.page.locator("input[name=\"country\"]").click()
        self.page.locator("input[name=\"country\"]").fill(country)

    def enter_phone_num(self, phone_num):
        self.page.locator("input[name=\"phoneNumber\"]").click()
        self.page.locator("input[name=\"phoneNumber\"]").fill(phone_num)

    def enter_dob(self, year, date):
        self.page.get_by_placeholder("DD.MM.YYYY").click()
        self.page.get_by_role("combobox").nth(1).select_option(year)
        self.page.get_by_label(date).click()

    def enter_address(self, address):
        self.page.locator("input[name=\"address\"]").click()
        self.page.locator("input[name=\"address\"]").fill(address)

    def select_gender(self, gender_option):
        self.page.get_by_label("Gender").select_option(gender_option)

    def click_accept_the_terms(self):
        self.page.get_by_role("checkbox").click()

    def click_register(self):
        self.page.get_by_role("button", name="Registriraj me").click()
