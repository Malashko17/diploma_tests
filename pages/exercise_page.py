from pages.base_page import BasePage
from pages.locators import exercise_page_locators as epl
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExercisePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_an_exercise_page(self):
        self.driver.get(self.exercise_url)

    @property
    def check_exercise_page_title(self):
        exercise_title = self.find_elements(epl.exercise_page_title)
        exercise_title_text = exercise_title[1].text
        return 'Упражнения' in exercise_title_text

    def open_description_of_a_specific_exercise(self):
        catalog_of_exercises = self.find_elements(epl.exercise_catalog)
        press_btn = catalog_of_exercises[8].click()
        self.scroll_the_page_to_the_middle()
        ex = self.find_element(epl.press_ex1).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(epl.press_description))

    def check_that_exercise_description_is_displayed(self):
        return self.find_element(epl.press_description).is_displayed()

    def open_statistics_of_exercise(self):
        statistics_btn = self.find_element(epl.description_statistics_btn).click()

    def check_that_statistics_info_is_displayed(self):
        return self.find_element(epl.info_statistics).is_displayed()

    def open_history_of_exercise(self):
        history_btn = self.find_element(epl.description_history_btn).click()

    def check_that_history_info_is_displayed(self):
        info = self.find_element(epl.info_history)
        info_text = info.get_attribute('innerText')
        return 'История упражнения пуста' in info_text

    def add_a_personal_exercise(self, personal_ex):
        self.find_element(epl.oneself_exercises).click()
        self.find_element(epl.new_exercise_field).send_keys(personal_ex)
        self.find_element(epl.add_new_exercise_button).click()

    def check_pop_up_message_that_a_personal_exercise_was_added(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(epl.pop_up_message)),
                   message='pop-up message "exercise added" did not appear')
        return True

    def setting_a_personal_exercise(self, type_of_ex):
        select = Select(self.find_element(epl.type_of_exercise_field))
        select.select_by_visible_text(type_of_ex)
        save = self.find_element(epl.save_exercise_details).click()

    def check_pop_up_message_that_a_personal_exercise_was_saved(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(epl.pop_up_message)),
                   message='pop-up message "saved" did not appear')
        return True

    def delete_a_personal_exercise(self):
        delete_btn = self.find_element(epl.delete_exercise).click()
        self.find_element(epl.yes_delete_exercise).click()

    def check_that_a_personal_exercise_was_deleted(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.invisibility_of_element_located(epl.pop_up_message)),
                   message='pop-up message "deleted" did not appear')
        return True

    def cancel_deletion_of_a_personal_exercise(self):
        delete_btn = self.find_element(epl.delete_exercise).click()
        self.find_element(epl.no_delete_exercise).click()

    def check_that_a_personal_exercise_still_displayed(self):
        return self.find_element(epl.saved_personal_exercise).is_displayed()

    def make_a_positive_search_of_exercise(self):
        self.find_element(epl.search_button).click()
        self.find_element(epl.search_exercise_field).send_keys('Приседания')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(epl.positive_search_result))

    def check_positive_search_result(self):
        result_of_search = self.find_element(epl.positive_search_result)
        text_of_search_result = result_of_search.get_attribute('innerText')
        split_text = text_of_search_result.split('\n')
        for exercise in split_text:
            if 'Приседания' or 'приседания' in exercise:
                return True

    def make_a_negative_search_of_exercise(self):
        self.find_element(epl.search_button).click()
        self.find_element(epl.search_exercise_field).send_keys('ghbctlfybz')
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(epl.negative_search_result))

    def check_negative_search_result_message(self):
        result_of_search = self.find_element(epl.negative_search_result)
        text_of_search_result = result_of_search.get_attribute('innerText')
        return 'Упражнение не найдено' in text_of_search_result






