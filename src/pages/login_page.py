from playwright.sync_api import Page, expect

from utils.config import URL, inventory_url


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')
        self.inventory_list = page.locator(".inventory_list")

    def open(self):
        self.page.goto(URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_empty(self):
        self.login_button.click()

    def assert_error_visible(self):
        expect(self.error_message).to_be_visible()

    def assert_inventory_page_opened(self):
        expect(self.page).to_have_url(inventory_url)
        expect(self.inventory_list).to_be_visible()
