import pytest
from selenium import webdriver

from pages.create_new_customer_page import CreateNewCustomer
from pages.customer_login_page import CustomerLogin
from pages.eco_friendly_page import EcoFriendly
from pages.sale_page import Sale


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)


@pytest.fixture()
def customer_login_page(driver):
    return CustomerLogin(driver)


@pytest.fixture()
def create_new_customer_page(driver):
    return CreateNewCustomer(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendly(driver)
