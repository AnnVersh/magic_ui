import allure


@allure.feature('Eco Friendly Section')
def test_correct_subsection_name(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_subsection_name('Eco Friendly')


@allure.feature('Eco Friendly Section')
def test_menu_eco_option_is(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_menu_eco_option('ECO COLLECTION')


@allure.feature('Eco Friendly Section')
def test_reviews_subsection_opens(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_reviews_subsection_opens('#reviews')
