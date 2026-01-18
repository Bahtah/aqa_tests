import allure
import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.test_data import VALID_USER, INVALID_PASSWORD_USER, LOCKED_USER, PERFORMANCE_GLITCH_USER


@allure.feature("Authorization")
class TestLogin:


    @allure.story("Successful login")
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(**VALID_USER)

        inventory_page = InventoryPage(page)
        assert inventory_page.is_opened()

    @allure.story("Login with empty fields")
    def test_login_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login_empty()
        expect(login_page.error_message).to_be_visible()

    @allure.story("Login with performance glitch user")
    def test_login_performance_glitch_user(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(**PERFORMANCE_GLITCH_USER)

        inventory_page = InventoryPage(page)
        assert inventory_page.is_opened()

    @pytest.mark.parametrize(
        "user",
        [INVALID_PASSWORD_USER, LOCKED_USER]
    )
    def test_login_with_invalid_credentials(self, page, user):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login(**user)
        expect(login_page.error_message).to_be_visible()


