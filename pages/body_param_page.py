from pages.base_page import BasePage
from pages.locators import body_param_page_locators as bppl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BodyParam(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_body_param_page(self):
        self.driver.get(self.body_param_url)

    def add_weight_param_2_december(self, value):
        parameter_list = self.find_elements(bppl.list_of_param)
        weight = parameter_list[1].click()
        weight_calendar_btn = self.find_elements(bppl.parameter_calendars)
        weight_calendar_btn[1].click()
        weight_calendar = self.find_elements(bppl.param_2_december)
        weight_calendar[1].click()
        value_fields = self.find_elements(bppl.parameter_value_fields)
        weight_value_field = value_fields[0].send_keys(value)
        weight_record_button = self.find_elements(bppl.parameter_record_button)
        weight_record_button[0].click()

    def check_that_weight_parameter_table_was_displayed(self):
        weight_table_info = self.find_elements(bppl.displayed_parameter_tables)
        return weight_table_info[1].is_displayed()

    def check_pop_up_message_that_param_was_saved(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(bppl.pop_up_message)),
                   message='pop-up message "saved" did not appear')
        return True







