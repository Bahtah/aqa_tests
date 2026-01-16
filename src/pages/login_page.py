from playwright.sync_api import Page, expect

from utils.config import URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto(URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_empty(self) -> None:
        self.login_button.click()

    def assert_error_visible(self) -> None:
        expect(self.error_message).to_be_visible()

