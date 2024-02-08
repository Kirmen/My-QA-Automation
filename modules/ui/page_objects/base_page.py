from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from conftest import BASE_DIR, DRIVER


class BasePage:
    PATH = BASE_DIR
    DRIVER_NAME = DRIVER

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=Service(self.PATH + self.DRIVER_NAME))

    def close(self):
        self.driver.close()
