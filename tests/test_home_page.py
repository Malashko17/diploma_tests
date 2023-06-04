from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.food_diary_page import FoodDiary
from pages.exercise_page import ExercisePage
import pytest
import allure


# @allure.severity(allure.severity_level.CRITICAL)
# @allure.feature('Registration')
# @allure.story('Testing the registration page')
# @pytest.mark.registration
# def test_go_to_the_registration_page(driver):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_registration_page()
#     registration_page = RegistrationPage(driver)
#     assert registration_page.check_that_jump_to_the_registration_page_was_completed
#
#
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.feature('Login')
# @allure.story('Testing the login page')
# @pytest.mark.login
# def test_go_to_the_login_page(driver):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_login_page()
#     login_page = LoginPage(driver)
#     assert login_page.check_that_jump_to_the_login_page_was_completed


# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_all_days_of_the_month_workout_are_displayed(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.show_all_days_of_the_month_workout()
#     assert home_page.check_that_all_dates_of_the_month_are_displayed()


# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_open_the_block_of_exercises(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.show_all_days_of_the_month_workout()
#     home_page.open_the_block_of_exercises()
#     assert home_page.check_that_the_window_of_exercises_was_opened()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_adding_exercise(driver, login):
#     home_page = HomePage(driver)
#     with allure.step('Open home page'):
#         home_page.open_home_page()
#     with allure.step('Show all days of the month'):
#         home_page.show_all_days_of_the_month_workout()
#     with allure.step('Open the block of exercises'):
#         home_page.open_the_block_of_exercises()
#     with allure.step('Adding an exercise to the workout'):
#         home_page.adding_an_exercise_to_the_workout()
#     assert home_page.check_that_selected_exercise_was_displayed()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_add_an_exercise_approach(driver, login):
#     home_page = HomePage(driver)
#     with allure.step('Open home page'):
#         home_page.open_home_page()
#     with allure.step('Show all days of the month'):
#         home_page.show_all_days_of_the_month_workout()
#     with allure.step('Open the block of exercises'):
#         home_page.open_the_block_of_exercises()
#     with allure.step('Adding an exercise to the workout'):
#         home_page.adding_an_exercise_to_the_workout()
#     with allure.step('Adding an exercise approach'):
#         home_page.add_an_exercise_approach()
#     assert home_page.check_that_an_exercise_approaches_were_added()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_add_a_comment_to_the_exercise(driver, login):
#     home_page = HomePage(driver)
#     with allure.step('Open home page'):
#         home_page.open_home_page()
#     with allure.step('Show all days of the month'):
#         home_page.show_all_days_of_the_month_workout()
#     with allure.step('Add a comment to the exercise'):
#         home_page.add_a_comment_to_the_exercise()
#     assert home_page.check_that_added_comment_was_displayed()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Home')
# @allure.story('Testing the home page')
# @pytest.mark.home
# def test_remove_the_selected_exercise(driver, login):
#     home_page = HomePage(driver)
#     with allure.step('Open home page'):
#         home_page.open_home_page()
#     with allure.step('Show all days of the month'):
#         home_page.show_all_days_of_the_month_workout()
#     with allure.step('Remove the selected exercise'):
#         home_page.remove_the_selected_exercise()
#     assert home_page.check_removal_of_exercise()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Exercises')
# @allure.story('Testing the exercises page')
# @pytest.mark.exercises
# def test_go_to_the_catalog_of_exercises_page(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_catalog_of_exercises_page()
#     exercise_page = ExercisePage(driver)
#     assert exercise_page.check_exercise_page_title
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Nutrition')
# @allure.story('Testing the nutrition page')
# @pytest.mark.nutrition
# def test_go_to_the_food_diary_page(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_food_diary_page()
#     food_diary = FoodDiary(driver)
#     assert food_diary.check_food_diary_page_title
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Body parameters')
# @allure.story('Testing the body parameters page')
# @pytest.mark.body_parameters
# def test_go_to_the_body_param_page(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_body_param_page()
#     assert home_page.check_that_jump_to_the_body_param_page_was_completed()
#
#
# @allure.severity(allure.severity_level.NORMAL)
# @allure.feature('Notes')
# @allure.story('Testing the notes page')
# @pytest.mark.notes
# def test_go_to_the_notes_page(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.go_to_the_notes_page()
#     assert home_page.check_that_jump_to_the_notes_page_was_completed()
#
#
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.feature('Profile settings')
# @allure.story('Testing the profile settings page')
# @pytest.mark.profile_settings
# def test_profile_dropdown_settings(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.profile_dropdown_settings()
#     assert home_page.check_that_profile_settings_were_opened()
#
#
# @allure.severity(allure.severity_level.CRITICAL)
# @allure.feature('Profile settings')
# @allure.story('Testing the profile settings page')
# @pytest.mark.logout
# # @pytest.mark.skip('Run only at the end of testing')
# def test_profile_dropdown_exit(driver, login):
#     home_page = HomePage(driver)
#     home_page.open_home_page()
#     home_page.profile_dropdown_exit()
#     assert home_page.check_that_login_button_is_displayed()








