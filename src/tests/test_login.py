import allure
from pages.login_page import LoginPage


@allure.feature("Authorization")
class TestLogin:


    @allure.story("Successful login")
    def test_successful_login(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        login_page.assert_inventory_page_opened()

    @allure.story("Login with invalid password")
    def test_login_with_invalid_password(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "wrong_password")
        login_page.assert_error_visible()

    @allure.story("Login with locked out user")
    def test_login_locked_out_user(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")
        login_page.assert_error_visible()

    @allure.story("Login with empty fields")
    def test_login_empty_fields(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login_empty()
        login_page.assert_error_visible()

    @allure.story("Login with performance glitch user")
    def test_login_performance_glitch_user(self, page):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login("performance_glitch_user", "secret_sauce")
        login_page.assert_inventory_page_opened()
