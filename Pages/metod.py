import time
from playwright.sync_api import Page, expect



class BasePage(object):

    def __init__(self, page: Page):
        self.page = page


class PageMetod(BasePage):

    def __init__(self, page):
        super().__init__(page)


    def open_koshelek_ru(self):
        url = self.page.goto('https://koshelek.ru/authorization/signup')
        expect(self.page).to_have_url('https://koshelek.ru/authorization/signup')


    def curent_url(self):
        url = self.page.url
        return url

    def get_by_lebel_clik(self, name):
        self.page.get_by_label(name).click()


    def text_fill_user_name(self, text):
        self.page.get_by_label("userName").fill(text)

    def text_fill_get_by_label(self, text, pole):
        self.page.get_by_label(pole).fill(text)

    def inpud_value_user(self):
        text = self.page.get_by_label("userName").input_value()
        return text

    def inpud_value_user_get_by_label(self, pole):
        text = self.page.get_by_label(pole).input_value()
        return text

    def inpud_clear_user(self):
        self.page.get_by_label("userName").clear()

    def inpud_clear_user_page_get_by_label(self, pole):
        self.page.get_by_label(pole).clear()

    """Методы с ошибками для сравнения в тестах"""
    def eror_maximum_characters_exceeding(self):
        text = self.page.get_by_text("maximumCharactersExceeding").text_content()
        return text

    def eror_invalid_user_name(self):
        text = self.page.get_by_text("invalidUserName").text_content()
        return text

    def eror_unavailable_characters(self):
        text = self.page.get_by_text("unavailableCharacters").text_content()
        return text

    def eror_field_is_empty(self):
        text = self.page.get_by_text("fieldIsEmpty").text_content()
        return text

    def eror_wrong_email_format(self):
        text = self.page.get_by_text("wrongEmailFormat").text_content()
        return text