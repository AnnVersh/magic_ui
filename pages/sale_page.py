from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc

import allure


class Sale(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.wait_until_visible(loc.header_title_loc)
        with allure.step(f'Check the header title is {text}'):
            assert header_title.text == text

    def check_link_text_womens_sale_is_correct(self, link_text):
        text_on_page = self.wait_until_visible(loc.womens_deals_loc)
        with allure.step(
                f"Check the women's sale link text is {link_text}"
        ):
            assert text_on_page.text == link_text

    def check_link_text_mens_sale_is_correct(self, link_text):
        text_on_page = self.wait_until_visible(loc.mens_deals_loc)
        with allure.step(
                f"Check the men's sale link text is {link_text}"
        ):
            assert text_on_page.text == link_text

    def check_discount_20_is(self, text):
        discount_text = self.wait_until_visible(loc.discount_20_off)
        with allure.step(f'Check the discount text is {text}'):
            assert discount_text.text == text
