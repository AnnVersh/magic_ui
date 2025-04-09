from pages.base_page import BasePage
from pages.locators import ecofriendly_locators as loc


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_subsection_name(self):
        subsection_name = self.find(loc.eco_friendly_subsection)
        assert subsection_name.text == "Eco Friendly"

    def check_menu_eco_option(self):
        menu_option = self.find(loc.eco_collection_menu_option)
        assert menu_option.text == 'ECO COLLECTION'

    def check_reviews_subsection_opens(self):
        self.find(loc.product_reviews).click()
        self.url_contains('#reviews')
