from selenium.webdriver.common.by import By

header_title_loc = (By.TAG_NAME, 'h1')
womens_deals_loc = (By.CLASS_NAME, 'more.button')
mens_deals_loc = (
    By.XPATH,
    '//a[@class="block-promo sale-mens"]'
    '//span[contains(@class, "more") and text()="Shop Men’s Deals"]'
)
discount_20_off = (
    By.XPATH,
    '//a[@class="block-promo sale-20-off"]'
    '//strong[contains(@class, "title") and text()="20% OFF"]'
)
