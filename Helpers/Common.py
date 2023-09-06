from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Union

typeWebDriver = Union[webdriver.Firefox,
                      webdriver.Chrome,
                      webdriver.Safari
]


# locator = ".topic_list th:nth-child(1)"
class Common():
    def __init__(self, driver: typeWebDriver):
        self.driver: typeWebDriver = driver
        self.driver.get("https://www.saucedemo.com")

    def presance_of_element(self, by: By, locator: str, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by.CSS_SELECTOR, locator)))

    def element_to_be_clickable(self, by: By, locator: str, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by.CSS_SELECTOR, locator)))

    def element_to_be_selected(self, by: By, locator: str, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_selected((by.CSS_SELECTOR, locator)))

    def __del__(self):
        self.driver.quit()
