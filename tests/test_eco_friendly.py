def test_correct_subsection_name(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_subsection_name()


def test_menu_eco_option_is(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_menu_eco_option()


def test_reviews_subsection_opens(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.check_reviews_subsection_opens()
