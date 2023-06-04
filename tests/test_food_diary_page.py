import pytest
import allure
from pages.food_diary_page import FoodDiary


CREDENTIALS = [
    {'product': 'Йогурт', 'choice': 3, 'weight': 150},
    {'product': 'Куриная грудка', 'choice': 1, 'weight': 100},
    {'product': 'Брокколи', 'choice': 4, 'weight': 170}]


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Nutrition')
@allure.story('Testing the nutrition page')
@pytest.mark.nutrition
@pytest.mark.parametrize('creds', CREDENTIALS)
def test_fill_in_a_food_diary(driver, login, creds):
    food_diary = FoodDiary(driver)
    food_diary.open_food_diary_page()
    food_diary.fill_in_a_food_diary(product=creds['product'],
                                    choice=creds['choice'],
                                    weight=creds['weight'])
    assert food_diary.check_that_total_calories_field_was_changed()
    assert food_diary.check_that_nutrition_list_is_displayed_after_addition()



