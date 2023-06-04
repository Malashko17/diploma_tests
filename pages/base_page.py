from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://www.gympad.ru/'
        self.registration_url = 'https://www.gympad.ru/registration/'
        self.login_url = 'https://www.gympad.ru/login'
        self.food_diary_url = 'https://www.gympad.ru/diary/nutrition/edit/month/11/year/2022/day/28'
        self.profile_settings_url = 'https://www.gympad.ru/settings'
        self.notes_url = 'https://www.gympad.ru/notes'
        self.exercise_url = 'https://www.gympad.ru/exercises'
        self.body_param_url = 'https://www.gympad.ru/bodyparams'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_elements(by_name, by_val)

    def scroll_the_page_to_the_bottom(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def scroll_the_page_to_the_middle(self):
        return self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2);")



