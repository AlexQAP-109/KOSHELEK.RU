from Pages.metod import PageMetod
import pytest

@pytest.fixture()
def start(page):
    page = PageMetod(page)
    page.open_koshelek_ru()
    return page


