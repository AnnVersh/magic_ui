from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    return chrome_driver
