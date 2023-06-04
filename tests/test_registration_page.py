import random
import time

from pages.registration_page import RegistrationPage
from pages.home_page import HomePage
import settings
import pytest
import allure


@allure.feature("Регистрация пользователя")
class TestRegistration:
    @allure.title("Регистрация с корректными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.registration
    def test_with_correct_registration_data(self, driver):
        reg_page = RegistrationPage(driver)
        with allure.step("Открыть страницу регистрации"):
            reg_page.open_registration_page()
        with allure.step("Заполнить поля регистрации"):
            reg_page.enter_correct_registration_data(email=f"{random.randint(1,1000)}@yandex.ru",
                                                     first_name=settings.first_name,
                                                     password='12345',
                                                     last_name="kin")
        with allure.step("Открыть главную страницу"):
            home_page = HomePage(driver)
        time.sleep(3)
        with allure.step("Ожидаемый результат: Имя зарегистрированного пользователя расположено "
                         "в правом верхнем углу"):
            assert home_page.check_that_username_is_displayed_in_the_welcome_block

    @allure.title("Проверка сообщения с ошибкой после регистрации с существующим email")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.registration
    def test_alert_message_after_registration_with_the_same_email(self, driver):
        reg_page = RegistrationPage(driver)
        with allure.step("Открыть страницу регистрации"):
            reg_page.open_registration_page()
        with allure.step("Ввести данные для регистрации с существующим email в системе"):
            reg_page.enter_correct_registration_data(email=settings.email,
                                                     first_name=settings.first_name,
                                                     password=settings.password,
                                                     last_name=settings.last_name)
        with allure.step("Ожидаемый результат: Отображается сообщение о ошибке"):
            assert reg_page.check_alert_message_after_registration_with_the_same_email()

