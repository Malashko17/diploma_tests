from pages.exercise_page import ExercisePage
import pytest
import allure


@allure.feature("План упражнений")
class TestExercises:
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_open_description_of_a_specific_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.open_description_of_a_specific_exercise()
        assert exercise_page.check_that_exercise_description_is_displayed()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_open_statistics_of_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.open_description_of_a_specific_exercise()
        exercise_page.open_statistics_of_exercise()
        assert exercise_page.check_that_statistics_info_is_displayed()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_open_history_of_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.open_description_of_a_specific_exercise()
        exercise_page.open_history_of_exercise()
        assert exercise_page.check_that_history_info_is_displayed()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_add_a_personal_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.add_a_personal_exercise(personal_ex='Пробежка')
        assert exercise_page.check_pop_up_message_that_a_personal_exercise_was_added()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_setting_a_personal_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.add_a_personal_exercise(personal_ex='HIIT')
        exercise_page.setting_a_personal_exercise(type_of_ex='Кардио (мин)')
        assert exercise_page.check_pop_up_message_that_a_personal_exercise_was_saved()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_delete_a_personal_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.add_a_personal_exercise(personal_ex='HIIT')
        exercise_page.delete_a_personal_exercise()
        assert exercise_page.check_that_a_personal_exercise_was_deleted()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_cancel_deletion_of_a_personal_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.add_a_personal_exercise(personal_ex='HIIT')
        exercise_page.cancel_deletion_of_a_personal_exercise()
        assert exercise_page.check_that_a_personal_exercise_still_displayed()


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_make_a_positive_search_of_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.make_a_positive_search_of_exercise()
        assert exercise_page.check_positive_search_result()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.exercises
    def test_make_a_negative_search_of_exercise(self, driver, login):
        exercise_page = ExercisePage(driver)
        exercise_page.open_an_exercise_page()
        exercise_page.make_a_negative_search_of_exercise()
        assert exercise_page.check_negative_search_result_message()