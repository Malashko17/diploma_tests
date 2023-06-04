from selenium.webdriver.common.by import By

add_notes_button = (By.CSS_SELECTOR, 'a[href="/notes/new"]')
note_name_field = (By.ID, 'noteTitle')
note_content_field = (By.CSS_SELECTOR, 'div[class="redactor_form-control redactor_editor"]')
note_save_button = (By.CSS_SELECTOR, 'button[type="submit"]')
note_content = (By.CSS_SELECTOR, 'div[class="content"]')
edit_note_content = (By.CSS_SELECTOR, 'a[class="btn btn-default"]')
delete_note_content = (By.CSS_SELECTOR, 'a[class="btn btn-default noteDelete"]')
yes_delete_button = (By.CSS_SELECTOR, 'button[class="btn btn-default"]')
note_display_field = (By.CLASS_NAME, 'notesEmpty')
no_delete_button = (By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
bold_font_button = (By.CSS_SELECTOR, 'a[title="Полужирный"]')
edit_font_to_bold_motivation = (By.TAG_NAME, 'strong')
italic_font_button = (By.CSS_SELECTOR, 'a[title="Наклонный"]')
edit_font_to_italic_motivation = (By.TAG_NAME, 'em')
list_of_added_notes = (By.CSS_SELECTOR, 'div[class="noteItem"]')
to_the_notes_button = (By.CSS_SELECTOR, 'a[class="back"]')

