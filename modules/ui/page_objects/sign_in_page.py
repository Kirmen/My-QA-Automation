from selenium.webdriver.common.by import By

from conftest import GITHUB_LOGIN_URL, NOVAPOSHTA_LOGIN_URL
from modules.ui.page_objects.base_page import BasePage


class GitHubSignInPage(BasePage):
    URL = GITHUB_LOGIN_URL

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def try_login(self, username, password):
        login_el = self.driver.find_element(By.ID, 'login_field')
        password_el = self.driver.find_element(By.ID, 'password')
        button_el = self.driver.find_element(By.NAME, 'commit')

        login_el.send_keys(username)
        password_el.send_keys(password)
        button_el.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title


class NovaPoshtaSignInPage(BasePage):
    URL = NOVAPOSHTA_LOGIN_URL

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(self.URL)

    def try_login(self, phone_number):
        phone_el = self.driver.find_element(By.ID, 'mat-input-0')
        button_el = self.driver.find_element(By.CSS_SELECTOR,
                                             '.mat-focus-indicator.continue-button.mat-raised-button.mat-button-base.mat-primary')

        phone_el.send_keys(phone_number)
        button_el.click()

    def check_url(self, expected_url):
        return self.driver.current_url == expected_url

    def check_error_message(self, expected_message):
        err_mess_el = self.driver.find_element(By.ID, 'mat-error-0')
        return err_mess_el.text == expected_message
