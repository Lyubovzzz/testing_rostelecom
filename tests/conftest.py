import pytest
from selenium import webdriver
import uuid


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture
def web_browser(request, driver):

    browser = driver
    browser.set_window_size(1400, 1000)

    # Вернуть объект браузера
    yield browser

