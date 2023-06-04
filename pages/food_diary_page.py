from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import food_diary_page_locators as fdpl


class FoodDiary(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_food_diary_page(self):
        self.driver.get(self.food_diary_url)

    @property
    def check_food_diary_page_title(self):
        diary_title = self.find_elements(fdpl.food_diary_page_title)
        diary_title_text = diary_title[1].text
        return 'Дневник питания' in diary_title_text

    def fill_in_a_food_diary(self, product, choice, weight):
        self.find_element(fdpl.calendar_right_btn).click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element(fdpl.month_name, 'декабрь 2022'))
        december_2 = self.find_element(fdpl.nutrition_2_december).click()
        product_name_field = self.find_element(fdpl.food_name_field).send_keys(product)
        product_list = self.find_elements(fdpl.list_of_suggested_products)
        ActionChains(self.driver).move_to_element(product_list[choice]).click().perform()
        self.find_element(fdpl.weight_field).send_keys(weight)
        self.scroll_the_page_to_the_middle()
        self.find_element(fdpl.add_product).click()

    def check_that_total_calories_field_was_changed(self):
        info = self.find_element(fdpl.total_calories_field).text
        return info != 0

    def check_that_nutrition_list_is_displayed_after_addition(self):
        return self.find_element(fdpl.displayed_nutrition_list_after_addition).is_displayed()











