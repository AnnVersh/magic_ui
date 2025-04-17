from pages.base_page import BasePage
from pages.customer_account_page import CustomerAccountPage as CA
from pages.locators import create_new_customer_locators as loc

import allure

from faker import Faker

fake = Faker()


class CreateNewCustomer(BasePage):
    page_url = '/customer/account/create/'

    def fill_in_first_name(self):
        with allure.step('Fill in the first name'):
            first_name = fake.first_name()
            first_name_field = self.find(loc.first_name_field_loc)
            first_name_field.send_keys(first_name)

    def fill_in_last_name(self):
        with allure.step('Fill in the last name'):
            last_name = fake.last_name()
            last_name_field = self.find(loc.last_name_field_loc)
            last_name_field.send_keys(last_name)

    def fill_in_email(self):
        with allure.step('Fill in the email'):
            email = fake.email()
            email_field = self.find(loc.email_field_loc)
            email_field.send_keys(email)

    def fill_in_invalid_email(self, email):
        with allure.step('Fill in an invalid email'):
            email_field = self.find(loc.email_field_loc)
            email_field.send_keys(email)

    def fill_in_password(self, password):
        with allure.step('Fill in the password'):
            password_field = self.find(loc.password_filed_loc)
            password_field.send_keys(password)

    def fill_in_confirm_password(
            self, password
    ):
        with allure.step('Fill in the confirmation password'):
            confirm_password_filed = self.find(
                loc.confirm_password_filed_loc
            )
            confirm_password_filed.send_keys(password)

    def submit_form(self):
        with allure.step('Submit the form'):
            self.find(loc.create_button_filed_loc).click()

    def fill_and_submit_valid_form(self, password):
        self.fill_in_first_name()
        self.fill_in_last_name()
        self.fill_in_email()
        self.fill_in_password(password)
        self.fill_in_confirm_password(password)
        self.submit_form()
        self.url_matches(self.base_url + CA.page_url)

    def check_not_matching_passwords_error(
            self,
            password,
            incorrect_confirm_password
    ):
        self.fill_in_password(password)
        self.fill_in_confirm_password(incorrect_confirm_password)
        self.submit_form()
        error = self.wait_until_visible(loc.password_confirmation_error)
        with allure.step('Check that the error message is displayed'):
            assert error.is_displayed()

    def check_invalid_email_error(self, email):
        self.fill_in_invalid_email(email)
        self.submit_form()
        error = self.wait_until_visible(loc.email_address_error)
        with allure.step('Check that the error message is displayed'):
            assert error.is_displayed()
