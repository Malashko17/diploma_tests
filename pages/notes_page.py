from pages.base_page import BasePage
from pages.locators import notes_page_locators as npl
from selenium.webdriver.common.keys import Keys
import settings


class NotesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_notes_page(self):
        self.driver.get(self.notes_url)

    def add_a_motivation_note(self):
        add_note_btn = self.find_element(npl.add_notes_button).click()
        name_field = self.find_element(npl.note_name_field)
        name_field.send_keys('Motivation')
        content_field = self.find_element(npl.note_content_field)
        content_field.send_keys(settings.motivation_note)
        save_btn = self.find_element(npl.note_save_button).click()

    def check_that_a_motivation_note_was_added(self):
        content_text = self.find_element(npl.note_content).text
        return settings.motivation_note in content_text

    def edit_a_motivation_note(self):
        edit_btn = self.find_element(npl.edit_note_content).click()
        content_field = self.find_element(npl.note_content_field)
        content_field.send_keys(settings.addition_to_motivation_note)
        save_btn = self.find_element(npl.note_save_button).click()

    def check_that_changes_in_motivation_note_were_displayed(self):
        edit_content_text = self.find_element(npl.note_content).text
        return settings.motivation_note and settings.addition_to_motivation_note in edit_content_text

    def delete_a_motivation_note(self):
        delete_btn = self.find_element(npl.delete_note_content).click()
        confirm_deletion = self.find_element(npl.yes_delete_button).click()

    def check_that_to_the_notes_button_is_displayed(self):
        return self.find_element(npl.to_the_notes_button).is_displayed()

    def check_that_a_motivation_note_was_deleted(self):
        return self.find_element(npl.add_notes_button).is_displayed()

    def cancel_deleting_a_motivation_note(self):
        delete_btn = self.find_element(npl.delete_note_content).click()
        cancel_deletion = self.find_element(npl.no_delete_button).click()

    def check_that_a_motivation_note_was_not_deleted(self):
        content_text = self.find_element(npl.note_content).text
        return settings.motivation_note in content_text

    def fill_in_the_content_field(self):
        add_note_btn = self.find_element(npl.add_notes_button).click()
        name_field = self.find_element(npl.note_name_field)
        name_field.send_keys('Motivation')
        content_field = self.find_element(npl.note_content_field)
        content_field.send_keys(settings.motivation_note)

    def change_font_to_bold_of_motivation_note_text(self):
        self.find_element(npl.note_content_field).send_keys(Keys.CONTROL + 'a')
        self.find_element(npl.bold_font_button).click()
        save_btn = self.find_element(npl.note_save_button).click()

    def check_that_font_of_motivation_note_has_become_bold(self):
        edit_font_content_to_bold = self.find_element(npl.edit_font_to_bold_motivation)
        bold_font_value = edit_font_content_to_bold.value_of_css_property('font-weight')
        return bold_font_value == '700'

    def change_font_to_italic_of_motivation_note_text(self):
        self.find_element(npl.note_content_field).send_keys(Keys.CONTROL + 'a')
        self.find_element(npl.italic_font_button).click()
        save_btn = self.find_element(npl.note_save_button).click()

    def check_that_font_of_motivation_note_has_become_italic(self):
        edit_font_content_to_italic = self.find_element(npl.edit_font_to_italic_motivation)
        italic_font_value = edit_font_content_to_italic.value_of_css_property('font-style')
        return italic_font_value == 'italic'







