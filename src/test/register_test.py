from playwright.sync_api import expect, sync_playwright
from src.pages.Register import RegisterPage
from src.pages.Login import LoginPage
from src.pages.Common import get_scrn_name
from src.pages.Common import get_webshop_link
from src.pages.Common import get_devices
from src.pages.Common import get_register_url
from src.pages.Common import get_login_url
import random
import string
import pytest

DEVICES = get_devices()
REGISTRIRAJ_SE = "Registriraj se na Tinel Workshop"
PRIJAVI_SE = "Prijavi se na Tinel Workshop"


# BUG#2 Mobile Registration Form cannot be accessed: Hidden by Left-side Image
@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize("device_type", DEVICES.keys())
def test_registration_verify_register_and_cancel_links(browser_type, device_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context(user_agent=DEVICES[device_type]['user_agent'])
        page = context.new_page()
        page.set_viewport_size({'width': DEVICES[device_type]['width'], 'height': DEVICES[device_type]['height']})
        register = RegisterPage(page)
        sc_path = get_scrn_name("test_registration_verify_register_and_cancel_links_" + device_type)

        register.navigate_to_register_page()
        page.screenshot(path=sc_path, full_page=True)
        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()

        page.get_by_role("button", name="Odustani").click()
        expect(page.get_by_text(PRIJAVI_SE)).to_be_visible()

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_success_mandatory_fields(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)
        login = LoginPage(page)
        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + "@gmail.com"
        sc_path = get_scrn_name("test_registration_success_mandatory_fields")

        register.navigate_to_register_page_from_login_page()
        register.enter_firstname("Ivan")
        register.enter_lastname("Ivic")
        register.enter_email(email)
        register.enter_password("Aaaa1234")
        register.confirm_password("Aaaa1234")
        register.enter_dob("2005", "Choose Wednesday, February 9th,")
        register.click_accept_the_terms()
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        expect(page.get_by_text(PRIJAVI_SE)).to_be_visible()
        login.provide_email_and_password(email, "Aaaa1234")

        expect(page).to_have_url(get_webshop_link())
        print("Expected URL after successful login is: " + get_webshop_link() + ". " +
              "Actual URL is: " + page.url)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_success_all_fields_valid_input(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)
        login = LoginPage(page)

        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + "@gmail.com"
        sc_path = get_scrn_name("test_registration_success_all_fields_valid_input")

        register.navigate_to_register_page_from_login_page()
        register.enter_firstname("Ivano")
        register.enter_lastname("Ivic")
        register.enter_email(email)
        register.enter_password("Aaaa1234")
        register.confirm_password("Aaaa1234")
        register.enter_zip("21000")
        register.enter_country("Croatia")
        register.enter_phone_num("098765432")
        register.enter_dob("2005", "Choose Wednesday, February 9th,")
        register.enter_address("Luka 25")
        register.select_gender("Male")
        register.click_accept_the_terms()
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        expect(page.get_by_text(PRIJAVI_SE)).to_be_visible()
        login.provide_email_and_password(email, "Aaaa1234")

        expect(page).to_have_url(get_webshop_link())
        print("Expected URL after successful login is: " + get_webshop_link() + ". " +
              "Actual URL is: " + page.url)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_failed_used_email(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)

        sc_path = get_scrn_name("test_registration_failed_used_email")

        register.navigate_to_register_page()
        register.enter_firstname("Jasmina")
        register.enter_lastname("Majstrovic")
        register.enter_email("jasmina@gmail.com")
        register.enter_password("Aaaa1234")
        register.confirm_password("Aaaa1234")
        register.enter_dob("2005", "Choose Wednesday, February 9th,")
        register.click_accept_the_terms()
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()
        print("Expected URL after successful login is: " + get_register_url() + ". " +
              "Actual URL is: " + page.url)

        # expect(page.get_by_text("Email je već zauzet. Molimo Vas da pokušate s drugom email adresom.")).to_be_visible()

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_failed_terms_unaccepted(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)
        sc_path = get_scrn_name("test_registration_failed_terms_unaccepted")

        register.navigate_to_register_page()
        register.enter_firstname("Jasmina")
        register.enter_lastname("Majstrovic")
        register.enter_email("jasmina@gmail.com")
        register.enter_password("Aaaa1234")
        register.confirm_password("Aaaa1234")
        register.enter_dob("2005", "Choose Wednesday, February 9th,")
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()
        print("Expected URL after successful login is: " + get_register_url() + ". " +
              "Actual URL is: " + page.url)

        context.close()
        browser.close()


# BUGS: 6-17 There is no validation of any input field within registration form
@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_failed_all_fields_invalid_input(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)

        email = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) + "@com.com"
        sc_path = get_scrn_name("test_registration_failed_all_fields_invalid_input")

        register.navigate_to_register_page()
        register.enter_firstname("!")
        register.enter_lastname("?")
        register.enter_email(email)
        register.enter_password("-+?aaaa")
        register.confirm_password("...............")
        register.enter_zip("a")
        register.enter_country("1")
        register.enter_phone_num(".")
        register.enter_dob("2028", "Choose Wednesday, February 9th,")
        register.enter_address(".1")
        register.select_gender("")
        register.click_accept_the_terms()
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        page.wait_for_timeout(1000)
        # page.screenshot(path=sc_path, full_page=True)
        expect(page.get_by_text(PRIJAVI_SE)).to_have_count(0)

        expect(page).to_have_url(get_register_url())
        print("Expected URL after failed registration is: " + get_register_url() + ". " +
              "Actual URL is: " + page.url)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_failed_empty_mandatory_fields(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)

        sc_path = get_scrn_name("test_registration_failed_empty_mandatory_fields")

        register.navigate_to_register_page_from_login_page()
        register.enter_firstname("")
        register.enter_lastname("")
        register.enter_email("")
        register.enter_password("")
        register.confirm_password("")
        register.click_accept_the_terms()
        register.click_register()
        page.screenshot(path=sc_path, full_page=True)

        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()
        expect(page.locator("span >> nth=1")).to_contain_text("Ime je obavezno")
        expect(page.locator("span >> nth=3")).to_contain_text("Prezime je obavezno")
        expect(page.locator("span >> nth=5")).to_contain_text("Obavezno polje")
        expect(page.locator("span >> nth=7")).to_contain_text("Obavezno polje")
        expect(page.locator("span >> nth=9")).to_contain_text("Obavezno polje")

        print("Expected URL after successful login is: " + get_register_url() + ". " +
              "Actual URL is: " + page.url)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_verify_tinel_workshop_image_link(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}  # Set the desired width and height
        )
        page = context.new_page()
        register = RegisterPage(page)
        sc_path = get_scrn_name("test_registration_verify_tinel_workshop_image_link")

        register.navigate_to_register_page()
        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()

        page.get_by_test_id("logo-link").dblclick()
        expect(page.get_by_text(PRIJAVI_SE)).to_be_visible()

        print("Expected URL after clicking on 'tinel workshop' image is: " + get_login_url() + ". "
              "Actual URL is: " + page.url)
        page.screenshot(path=sc_path, full_page=True)

        context.close()
        browser.close()


# BUG#3 impacts this test due to SVG element on the left side which partially hide "tinel Workshop" link
@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_failed_tinel_workshop_image_link_reduced_browser_size(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        # tablet in landscape orientation
        context = browser.new_context(
            viewport={'width': 1024, 'height': 500}  # Set the desired width and height
        )
        page = context.new_page()
        register = RegisterPage(page)
        sc_path = get_scrn_name("test_registration_failed_tinel_workshop_image_link_reduced_browser_size")

        register.navigate_to_register_page()
        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()

        page.screenshot(path=sc_path, full_page=True)
        page.get_by_test_id("logo-link").dblclick()
        expect(page.get_by_text(PRIJAVI_SE)).to_be_visible()

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_registration_verify_terms_and_conditions_link(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        register = RegisterPage(page)
        sc_path = get_scrn_name("test_registration_verify_terms_and_conditions_link")

        register.navigate_to_register_page()
        expect(page.get_by_text(REGISTRIRAJ_SE)).to_be_visible()

        page.get_by_role("link", name="Opće uvjete.").click()
        page.screenshot(path=sc_path, full_page=True)
        expect(page).not_to_have_url(get_register_url())

        # expect(page).to_have_url("https://qa-task-fe.vercel.app/terms-of-use")

        context.close()
        browser.close()


