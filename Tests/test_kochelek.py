import pytest


def test_url(start):
    "Тестируем урл"
    start.open_koshelek_ru()
    url = start.curent_url()
    assert url == 'https://koshelek.ru/authorization/signup'

"""Негативные проверки. Логика(при вводе текста в поле inpud UsserName, отрабатывает Js. и 
появляется текст ошибки. На основе этого, мы будем сравнивать результат)"""
def test_pole_usser1(start):
    """Проверяем поле usserName на ошибку maximumCharactersExceeding."""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('ddddddddddddddddddddddddddddddddddd')
    text1 = start.inpud_value_user()
    text_eror = start.eror_maximum_characters_exceeding()
    assert text_eror == ' maximumCharactersExceeding '
    assert text1 == 'ddddddddddddddddddddddddddddddddddd'


def test_pole_usser2(start):
    """Проверяем поле usserName на ошибку invalidUserName."""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('Вася')
    text = start.inpud_value_user()
    """Кликаем чтобы поле email чтобы появилась ошибка"""
    start.get_by_lebel_clik("email")
    text_eror = start.eror_invalid_user_name()
    assert text_eror == ' invalidUserName '
    assert text == 'Вася'


def test_pole_usser3(start):
    """Проверяем поле usserName на ошибку unavailableCharacters."""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('Федя')
    text = start.inpud_value_user()
    text_eror = start.eror_unavailable_characters()
    assert text_eror == ' unavailableCharacters '
    assert text == 'Федя'


def test_pole_usser4(start):
    """Проверяем поле usserName на ошибку fieldIsEmpty.(Сначала вводим данные, а потом очищаем поле и
    переходим к другому)"""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('AБВГ')
    text = start.inpud_value_user()
    start.inpud_clear_user()
    start.get_by_lebel_clik("email")
    text_eror = start.eror_field_is_empty()
    assert text_eror == ' fieldIsEmpty '
    assert text == 'AБВГ'


"""Поле email , негативные сценарии (поле usserName заполняем валидным значением)"""

def test_pole_email1(start):
    """Проверяем поле email на ошибку fieldIsEmpty.(Сначала вводим данные, а потом очищаем поле и
        переходим к другому)"""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('Testerqa')
    start.get_by_lebel_clik('email')
    start.text_fill_get_by_label('qwa', 'email')
    text_email = start.inpud_value_user_get_by_label('email')
    start.inpud_clear_user_page_get_by_label('email')
    start.get_by_lebel_clik('password')
    text_eror = start.eror_field_is_empty()
    assert text_eror == ' fieldIsEmpty '
    assert text_email == 'qwa'


def test_pole_email2(start):
    """Проверяем поле usserName на ошибку wrongEmailFormat."""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('Testerqa')
    start.get_by_lebel_clik('email')
    start.text_fill_get_by_label('qwa', 'email')
    text_email = start.inpud_value_user_get_by_label('email')
    start.get_by_lebel_clik('password')
    text_eror = start.eror_wrong_email_format()
    assert text_eror == ' wrongEmailFormat '
    assert text_email == 'qwa'

"""Параметризуем (так для примера)"""
@pytest.mark.parametrize('invalid_email', ['qva', 'sdfgshsgfsd', '3456dfghhgfd/'], ids=['qva', 'sdfgshsgfsd', '3456dfghhgfd/'])
def test_pole_email3(start, invalid_email):
    """Проверяем поле usserName на ошибку wrongEmailFormat."""
    start.open_koshelek_ru()
    start.get_by_lebel_clik('userName')
    start.text_fill_user_name('Testerqa')
    start.get_by_lebel_clik('email')
    start.text_fill_get_by_label(invalid_email, 'email')
    text_email = start.inpud_value_user_get_by_label('email')
    start.get_by_lebel_clik('password')
    text_eror = start.eror_wrong_email_format()
    assert text_eror == ' wrongEmailFormat '
    assert text_email == invalid_email



