from pages.base_page import BasePage
from pages.locators import ecofriendly_locators as loc

import allure


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_subsection_name(self, title):
        subsection_name = self.wait_until_visible(loc.eco_friendly_subsection)
        with allure.step(f'Check the subsection title is {title}'):
            assert subsection_name.text == title

    def check_menu_eco_option(self, eco_menu_option):
        menu_option = self.wait_until_visible(loc.eco_collection_menu_option)
        with allure.step(f'Check that menu text is {eco_menu_option}'):
            assert menu_option.text == eco_menu_option

    def check_reviews_subsection_opens(self, url_text):
        self.wait_until_visible(loc.product_reviews).click()
        self.url_contains(url_text)
