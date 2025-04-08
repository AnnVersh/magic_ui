from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import customer_login_locators as loc
from utils import project_ec


class CustomerLogin(BasePage):
    page_url = '/customer/account/login/'

    def fill_in_login_form(self, login, password):
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        sign_in_button = self.find(loc.sign_in_button_loc)
        email_field.send_keys(login)
        password_field.send_keys(password)
        sign_in_button.click()

    def check_error_alert_text_is(self, text):
        WebDriverWait(self.driver, 5).until(
            project_ec.text_is_not_empty_in_element(loc.error_locator)
        )
        error_alert = self.driver.find_element(*loc.error_locator)

        assert error_alert.text == text
