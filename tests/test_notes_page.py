from pages.notes_page import NotesPage
import allure
import pytest


@allure.feature('Заметки')
class TestNotes:

    @allure.title("Добавление заметки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_add_a_motivation_note(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.add_a_motivation_note()
        assert notes_page.check_that_a_motivation_note_was_added()

    @allure.title("Удаление заметки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_delete_a_motivation_note(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.add_a_motivation_note()
        assert notes_page.check_that_to_the_notes_button_is_displayed()
        notes_page.delete_a_motivation_note()
        assert notes_page.check_that_a_motivation_note_was_deleted()

    @allure.title("Отмена удаления заметки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_cancel_deleting_a_motivation_note(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.add_a_motivation_note()
        notes_page.cancel_deleting_a_motivation_note()
        assert notes_page.check_that_a_motivation_note_was_not_deleted()

    @allure.title("Редактирование заметки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_edit_a_motivation_note(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.add_a_motivation_note()
        notes_page.edit_a_motivation_note()
        assert False, "Поле ввода изменилось"

    @allure.title("Изменение шрифта текста заметки на жирный")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_change_font_to_bold_of_motivation_note_text(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.fill_in_the_content_field()
        notes_page.change_font_to_bold_of_motivation_note_text()
        assert notes_page.check_that_font_of_motivation_note_has_become_bold()

    @allure.title("Изменение шрифта текста заметки на курсив")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.notes
    def test_change_font_to_italic_of_motivation_note_text(self, driver, login):
        notes_page = NotesPage(driver)
        notes_page.open_notes_page()
        notes_page.fill_in_the_content_field()
        notes_page.change_font_to_italic_of_motivation_note_text()
        assert notes_page.check_that_font_of_motivation_note_has_become_italic()




