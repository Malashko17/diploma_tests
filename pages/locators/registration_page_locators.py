from selenium.webdriver.common.by import By

registration_and_enter_button = (By.ID, 'registration-submit')
email_field = (By.CSS_SELECTOR, 'input[name="email"]')
first_name_field = (By.NAME, 'first_name')
last_name_field = (By.NAME, 'last_name')
password_field = (By.NAME, 'new_password')
repeat_password_field = (By.NAME, 'new_repeat_password')
alert_message = (By.CLASS_NAME, 'alert-login')
