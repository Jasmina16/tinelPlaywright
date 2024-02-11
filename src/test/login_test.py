from playwright.sync_api import expect, sync_playwright
from src.pages.Login import LoginPage
from src.pages.Common import get_scrn_name
from src.pages.Common import get_devices
from src.pages.Common import get_webshop_link
import pytest

DEVICES = get_devices()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_login_verify_login_page_link(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        sc_path = get_scrn_name("test_login_verify_login_page_link")

        login.navigate()
        expect(page.get_by_role("button", name="Prijavi se")).to_be_visible()
        page.screenshot(path=sc_path, full_page=True)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_login_failure_empty_input(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        sc_path = get_scrn_name("test_login_failure_empty_input")

        login.navigate()
        login.provide_email_and_password("", "")

        expect(page.locator("span >> nth=1")).to_contain_text("Obavezno polje")
        expect(page.locator("span >> nth=3")).to_contain_text("Lozinka je obavezna")
        print("Expected feedback message is: Obavezno polje. "
              "Actual feedback message is: " + page.locator("span >> nth=1").text_content())
        print("Expected feedback message is: Lozinka je obavezna. "
              "Actual feedback message is: " + page.locator("span >> nth=3").text_content())
        page.screenshot(path=sc_path, full_page=True)

        context.close()
        browser.close()


@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
@pytest.mark.parametrize("device_type", DEVICES.keys())
def test_login_success_registered_user(browser_type, device_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context(user_agent=DEVICES[device_type]['user_agent'])
        page = context.new_page()
        page.set_viewport_size({'width': DEVICES[device_type]['width'], 'height': DEVICES[device_type]['height']})
        login = LoginPage(page)
        sc_path = get_scrn_name("test_login_success_registered_user_" + device_type)

        login.navigate()
        expect(page.locator("input[name=\"email\"]")).to_be_visible()
        expect(page.locator("input[name=\"password\"]")).to_be_visible()
        login.provide_email_and_password("jasmina@gmail.com", "jasmina1")

        expect(page).to_have_url(get_webshop_link())
        print("Expected URL after successful login is: " + get_webshop_link() + ". "
              "Actual URL is: " + page.url)

        page.screenshot(path=sc_path, full_page=True)

        context.close()
        browser.close()


# BUG#4 - test fails because no feedback message is shown if unregistered user attempt to log in
@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_login_failure_unregistered_user(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        login = LoginPage(page)
        sc_path = get_scrn_name("test_login_failure_unregistered_user")

        login.navigate()
        login.provide_email_and_password("tea@gmail.com", "tea12345")
        expect(page.get_by_role("button", name="Prijavi se")).to_be_visible()
        page.screenshot(path=sc_path, full_page=True)
        expect(page.locator("span >> nth=0")).to_contain_text("Nemamo korisnika registriranog s ovim emailom.")

        context.close()
        browser.close()


# BUG#1 - Fails because the whole input form is not shown
@pytest.mark.parametrize("browser_type", ['chromium', 'firefox', 'webkit'])
def test_login_failed_registered_user_reduced_browser_size(browser_type):
    with sync_playwright() as p:
        browser = getattr(p, browser_type).launch(headless=False)
        context = browser.new_context(
            viewport={'width': 1024, 'height': 500}  # Set the desired width and height
        )
        page = context.new_page()
        login = LoginPage(page)
        sc_path = get_scrn_name("test_login_failed_registered_user_reduced_browser_size_" + browser_type)

        login.navigate()
        expect(page.locator("input[name=\"email\"]")).to_be_visible()
        expect(page.locator("input[name=\"password\"]")).to_be_visible()
        login.provide_email_and_password("jasmina@gmail.com", "jasmina1")

        expect(page).to_have_url(get_webshop_link())
        print("Expected URL after successful login is: " + get_webshop_link() + ". "
              "Actual URL is: " + page.url)

        page.screenshot(path=sc_path, full_page=True)

        context.close()
        browser.close()
