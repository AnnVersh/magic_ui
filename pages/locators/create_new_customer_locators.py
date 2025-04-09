from selenium.webdriver.common.by import By

first_name_field_loc = (By.CSS_SELECTOR, '#firstname')
last_name_field_loc = (By.CSS_SELECTOR, '#lastname')
email_field_loc = (By.ID, 'email_address')
password_filed_loc = (By.ID, 'password')
confirm_password_filed_loc = (By.ID, 'password-confirmation')
create_button_filed_loc = (By.CLASS_NAME, 'action.submit.primary')
password_confirmation_error = (By.ID, 'password-confirmation-error')
email_address_error = (By.ID, 'email_address-error')
