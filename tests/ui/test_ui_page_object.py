import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from modules.ui.page_objects.sign_in_page import GitHubSignInPage, NovaPoshtaSignInPage


@pytest.mark.ui
def test_github_check_incorrect_username_page_object():
    sign_in_page = GitHubSignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login('kirmen_yo@gmail.com', 'incorrectpas')

    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    sign_in_page.close()


@pytest.mark.ui
def test_novaposhta_check_too_short_phone_number_page_object():
    sign_in_page = NovaPoshtaSignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login('09595')

    assert sign_in_page.check_error_message('Занадто короткий номер')

    sign_in_page.close()


@pytest.mark.ui
def test_novaposhta_check_empty_phone_number_page_object():
    sign_in_page = NovaPoshtaSignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login('')

    assert sign_in_page.check_error_message("Це поле обов'язкове")

    sign_in_page.close()


@pytest.mark.ui
def test_novaposhta_check_unregistered_phone_number_page_object():
    sign_in_page = NovaPoshtaSignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login('123456789')

    WebDriverWait(sign_in_page.driver, 10).until(
        expected_conditions.url_to_be(r"https://id.novaposhta.ua/registration")
    )

    assert sign_in_page.check_url(r"https://id.novaposhta.ua/registration")

    sign_in_page.close()
