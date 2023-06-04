import settings
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import profile_settings_page_locators as pspl


class ProfileSettings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_profile_setting_page(self):
        self.driver.get(self.profile_settings_url)

    def check_that_the_first_name_field_is_filled_in(self):
        first_name = self.find_element(pspl.first_name_field)
        first_name_value = first_name.get_attribute('value')
        return f'{settings.first_name}' in first_name_value

    def check_the_last_name_field_is_filled_in(self):
        last_name = self.find_element(pspl.last_name_field)
        last_name_value = last_name.get_attribute('value')
        return f'{settings.last_name}' in last_name_value

    def check_the_email_field_is_filled_in(self):
        email = self.find_element(pspl.email_field)
        email_value = email.get_attribute('value')
        return f'{settings.email}' in email_value

    def add_additional_user_info(self):
        femail = self.find_element(pspl.femail_box).click()
        birthday = self.find_element(pspl.birth_date)
        birthday.send_keys('03071989')
        self.find_element(pspl.save_info_btn).click()

    def check_pop_up_message_that_user_info_was_saved(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(pspl.pop_up_message)),
                   message='pop-up message "settings have been saved" did not appear')
        return True

    def change_existing_password(self):
        old_passwd = self.find_element(pspl.old_password_field)
        old_passwd.send_keys(settings.password)
        new_passwd = self.find_element(pspl.new_password_field)
        new_passwd.send_keys(settings.new_password)
        new_repeat_passwd = self.find_element(pspl.new_repeat_password)
        new_repeat_passwd.send_keys(settings.new_password)
        self.find_element(pspl.save_info_btn).click()

    def try_to_change_incorrect_password(self):
        old_passwd = self.find_element(pspl.old_password_field)
        old_passwd.send_keys('mistake')
        new_passwd = self.find_element(pspl.new_password_field)
        new_passwd.send_keys(settings.new_password)
        new_repeat_passwd = self.find_element(pspl.new_repeat_password)
        new_repeat_passwd.send_keys(settings.new_password)
        self.find_element(pspl.save_info_btn).click()

    def check_pop_up_message_that_password_was_not_saved(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(pspl.pop_up_message)),
                   message='pop-up message "error saving settings" did not appear')
        return True

    def check_that_help_message_is_appeared(self):
        help_message_text = self.find_element(pspl.help_block_message).text
        return 'Неправильный пароль.' in help_message_text










