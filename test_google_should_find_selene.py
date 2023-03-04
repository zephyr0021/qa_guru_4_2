from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def set_size_browser():
    browser.driver.set_window_size(200, 1200)


def test_first(open_browser, set_size_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_second(open_browser, set_size_browser):
    browser.element('[name="q"]').should(be.blank).type('werwed23423rwer23423423rewr2342352dsfds').press_enter()
    browser.element('[id="result-stats"').should(have.text('Результатов: примерно 0'))
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))

