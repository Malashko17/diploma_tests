from pages.base_page import BasePage
from pages.locators import login_page_locators as lpl


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.driver.get(self.login_url)

    @property
    def check_that_jump_to_the_login_page_was_completed(self):
        login_btn_text = self.find_element(lpl.login_button).text
        return 'Войти' in login_btn_text

    def enter_login_data(self, email, password):
        self.find_elements(lpl.all_login_fields)[0].send_keys(email)
        self.find_elements(lpl.all_login_fields)[1].send_keys(password)
        self.find_element(lpl.login_button).click()

    def check_alert_message_after_login_with_incorrect_password(self):
        alert_text = self.find_element(lpl.alert_message).text
        return 'Неправильный пароль' in alert_text

    def check_alert_message_after_login_with_incorrect_email(self):
        alert_text = self.find_element(lpl.alert_message).text
        return 'Пользователь не найден' in alert_text

    def check_that_remember_me_box_is_selected(self):
        return self.find_element(lpl.remember_me_box).is_selected()

    def check_that_forget_password_link_presents_on_the_login_page(self):
        return self.find_element(lpl.forget_password_link).is_enabled()

    def try_to_enter_with_a_new_password(self, email, new_password):
        self.find_elements(lpl.all_login_fields)[0].send_keys(email)
        self.find_elements(lpl.all_login_fields)[1].send_keys(new_password)
        self.find_element(lpl.login_button).click()



