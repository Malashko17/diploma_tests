from pages.profile_settings_page import ProfileSettings
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Profile settings')
@allure.story('Testing the profile settings page')
@pytest.mark.profile_settings
def test_the_correct_user_data_is_displayed(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    assert profile_settings_page.check_that_the_first_name_field_is_filled_in()
    assert profile_settings_page.check_the_last_name_field_is_filled_in()
    assert profile_settings_page.check_the_email_field_is_filled_in()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Profile settings')
@allure.story('Testing the profile settings page')
@pytest.mark.profile_settings
def test_add_additional_user_info(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.add_additional_user_info()
    profile_settings_page.scroll_the_page_to_the_middle()
    assert profile_settings_page.check_pop_up_message_that_user_info_was_saved()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Profile settings')
@allure.story('Testing the profile settings page')
@pytest.mark.profile_settings
def test_change_incorrect_password(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.try_to_change_incorrect_password()
    assert profile_settings_page.check_that_help_message_is_appeared()
    assert profile_settings_page.check_pop_up_message_that_password_was_not_saved()


@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('Profile settings')
@allure.story('Testing the profile settings page')
@pytest.mark.change_existing_password
# @pytest.mark.skip('Run only at the end of testing')
def test_change_existing_password(driver, login):
    profile_settings_page = ProfileSettings(driver)
    profile_settings_page.open_profile_setting_page()
    profile_settings_page.change_existing_password()
    assert profile_settings_page.check_pop_up_message_that_user_info_was_saved()





