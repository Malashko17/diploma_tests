from selenium.webdriver.common.by import By

food_diary_page_title = (By.CLASS_NAME, 'col-lg-12')
calendar_right_btn = (By.CSS_SELECTOR, 'a[id="calendarRight"]')
month_name = (By.LINK_TEXT, 'декабрь 2022')
nutrition_2_december = (By.LINK_TEXT, '2')
food_name_field = (By.ID, 'nutInput')
list_of_suggested_products = (By.CSS_SELECTOR, 'div[class="tt-suggestion tt-selectable"]')
weight_field = (By.ID, 'nutWeightInput')
add_product = (By.ID, 'nutSubmit')
total_calories_field = (By.ID, 'totalCalories')
displayed_nutrition_list_after_addition = (By.CSS_SELECTOR, 'ul[class="nutList"]')
