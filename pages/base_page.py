from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        with allure.step('Open a page'):
            if self.page_url:
                self.driver.get(f'{self.base_url}{self.page_url}')
            else:
                raise NotImplementedError(
                    "Page can't be opened for this page class"
                )

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_for_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url == expected_url
        )

    def current_url(self):
        return self.driver.current_url

    def url_matches(self, expected_url):
        with allure.step(
                f'Check that URL matches the required one:'
                f' {expected_url}'
        ):
            self.wait_for_url(expected_url)
        assert self.current_url() == expected_url

    def url_contains(self, expected_url_part):
        with allure.step(
                f'Check that URL contains the required part:'
                f' {expected_url_part}'
        ):
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(expected_url_part)
            )
        assert expected_url_part in self.current_url()

    def wait_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
