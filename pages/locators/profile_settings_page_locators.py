from selenium.webdriver.common.by import By

first_name_field = (By.NAME, 'User[first_name]')
last_name_field = (By.NAME, 'User[last_name]')
email_field = (By.NAME, 'User[email]')
femail_box = (By.CSS_SELECTOR, 'label[for="female"]')
birth_date = (By.NAME, 'User[birthday]')
save_info_btn = (By.CSS_SELECTOR, 'button[class="btn btn-orange ml10"]')
pop_up_message = (By.CSS_SELECTOR, 'div[class="sticky-queue top-right"]')
old_password_field = (By.NAME, 'User[old_password]')
new_password_field = (By.NAME, 'User[new_password]')
new_repeat_password = (By.NAME, 'User[new_repeat_password]')
help_block_message = (By.CSS_SELECTOR, 'span[class="help-block red"]')