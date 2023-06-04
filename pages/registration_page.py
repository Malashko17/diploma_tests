import settings
from pages.base_page import BasePage
from pages.locators import registration_page_locators as rpl


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_registration_page(self):
        self.driver.get(self.registration_url)

    @property
    def check_that_jump_to_the_registration_page_was_completed(self):
        registration_btn_text = self.find_element(rpl.registration_and_enter_button).text
        return 'Зарегистрироваться и войти' in registration_btn_text

    def enter_correct_registration_data(self, email, first_name, last_name, password):
        self.find_element(rpl.email_field).send_keys(email)
        self.find_element(rpl.first_name_field).send_keys(first_name)
        self.find_element(rpl.last_name_field).send_keys(last_name)
        self.find_element(rpl.password_field).send_keys(password)
        self.find_element(rpl.repeat_password_field).send_keys(password)
        self.find_element(rpl.registration_and_enter_button).click()

    def check_alert_message_after_registration_with_the_same_email(self):
        alert_text = self.find_element(rpl.alert_message).text
        return f'Емейл "{settings.email}" уже занят.' in alert_text



