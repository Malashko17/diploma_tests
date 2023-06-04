from pages.notes_page import NotesPage
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_add_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    assert notes_page.check_that_a_motivation_note_was_added()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_delete_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    assert notes_page.check_that_to_the_notes_button_is_displayed()
    notes_page.delete_a_motivation_note()
    assert notes_page.check_that_a_motivation_note_was_deleted()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_cancel_deleting_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    notes_page.cancel_deleting_a_motivation_note()
    assert notes_page.check_that_a_motivation_note_was_not_deleted()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_edit_a_motivation_note(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.add_a_motivation_note()
    notes_page.edit_a_motivation_note()
    assert notes_page.check_that_changes_in_motivation_note_were_displayed()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_change_font_to_bold_of_motivation_note_text(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.fill_in_the_content_field()
    notes_page.change_font_to_bold_of_motivation_note_text()
    assert notes_page.check_that_font_of_motivation_note_has_become_bold()


@allure.severity(allure.severity_level.NORMAL)
@allure.feature('Notes')
@allure.story('Testing the notes page')
@pytest.mark.notes
def test_change_font_to_italic_of_motivation_note_text(driver, login):
    notes_page = NotesPage(driver)
    notes_page.open_notes_page()
    notes_page.fill_in_the_content_field()
    notes_page.change_font_to_italic_of_motivation_note_text()
    assert notes_page.check_that_font_of_motivation_note_has_become_italic()




