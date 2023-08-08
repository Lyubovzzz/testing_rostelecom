import time
import pytest
from selenium.webdriver.common.by import By
import uuid
from config import *
from locators import *


def test_auth_by_vk(driver):
    """ Проверка, что иконка Вконтакте ведет на страницу авторизации через ВК """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_vk.by, locator_btn_vk.value).click()     # Ищем иконку вконтакте , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if auth_vk in driver.current_url:
        driver.save_screenshot('result_auth_vk.png')         # Если мы на странице авторизации, сделать скриншот
    else:
        raise Exception("Error auth")

def test_auth_by_ok(driver):
    """ Проверка, что иконка Одноклассники ведет на страницу авторизации через Одноклассники """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_ok.by, locator_btn_ok.value).click()     # Ищем иконку одноклассники , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if auth_ok in driver.current_url:
        driver.save_screenshot('result_auth_ok.png')         # Если мы на странице авторизации, сделать скриншот
    else:
        raise Exception("Error auth")

def test_auth_by_mail(driver):
    """ Проверка, что иконка Mail.ru ведет на страницу авторизации через Mail.ru """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_mail.by, locator_btn_mail.value).click()     # Ищем иконку Mail.ru , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if auth_mail in driver.current_url:
        driver.save_screenshot('result_auth_mail.png')         # Если мы на странице авторизации, сделать скриншот
    else:
        raise Exception("Error auth")

def test_auth_by_yandex(driver):
    """ Проверка, что иконка Yandex ведет на страницу авторизации через Yandex """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_yandex.by, locator_btn_yandex.value).click()     # Ищем иконку yandex , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if auth_yandex in driver.current_url:
        driver.save_screenshot('result_auth_yandex.png')         # Если мы на странице авторизации, сделать скриншот
    else:
        raise Exception("Error auth")

def test_link_to_user_agreement(driver):
    """ Проверка, что гиперссылка "пользовательское соглашение" ведет на страницу пользовательского соглашения """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_user_agreement.by, locator_user_agreement.value).click()     # Ищем ссылку на пользовательское соглашение , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if user_agreement == driver.current_url:
        driver.save_screenshot('result_user_agreement.png')         # Если мы на странице соглашения, сделать скриншот
    else:
        raise Exception("Error")


def test_link_to_user_agreement_in_footer(driver):
    """ Проверка, что гиперссылка "пользовательское соглашение" в подвале страницы ведет на страницу пользовательского соглашения """

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_user_agreement_footer.by, locator_user_agreement_footer.value).click()     # Ищем ссылку на пользовательское соглашение , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    if user_agreement == driver.current_url:
        driver.save_screenshot('result_user_agreement.png')         # Если мы на странице соглашения, сделать скриншот
    else:
        raise Exception("Error")

def test_button_forgot_password(driver):
    """ Проверка, что кнопка "Забыли пароль" ведет на страницу восстановления пароля"""

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_forgot_password.by, locator_btn_forgot_password.value).click()     # Ищем кнопку "Забыли пароль" , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    forgot_pass_passed = driver.find_element(locator_pass_recovery.by, locator_pass_recovery.value) # Находим элемент "Восстановление пароля"

def test_button_register(driver):
    """ Проверка, что кнопка "Зарегистрироваться" ведет на страницу регистрации"""

    driver.get(base_url)     # Открываем страницу для поиска:
    time.sleep(5)  # небольшая задержка

    search_button = driver.find_element(locator_btn_register.by, locator_btn_register.value).click()     # Ищем кнопку "Зарегистрироваться" , кликаем на нее:
    time.sleep(5)  # небольшая задержка

    register_passed = driver.find_element(locator_register.by, locator_register.value) # Находим элемент "Регистрация"

def test_auth_by_valid_email_and_pass(web_browser):
    """ Позитивная проверка. Ввод валидного емаил и пароля"""
    driver = web_browser

    driver.get(base_url)     # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_email = driver.find_element(locator_tab_email.by, locator_tab_email.value).click()     # Ищем кнопку "Почта" в табе, нажимаем на нее

    field_email = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода электронной почты, затем вводим некоректный email
    field_email.send_keys(valid_email)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(valid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    auth_passed = driver.find_element(locator_btn_logout.by, locator_btn_logout.value) # Проверка авторизации, есть кнопка "Выйти"

def test_auth_by_invalid_email_and_pass(web_browser):
    """ Негативная проверка. Ввод некорректных емаил и пароля"""
    driver = web_browser

    driver.get(base_url)     # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_email = driver.find_element(locator_tab_email.by, locator_tab_email.value).click()     # Ищем кнопку "Почта" в табе, нажимаем на нее

    field_email = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода электронной почты, затем вводим некоректный email
    field_email.send_keys(invalid_email)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(invalid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    error_message = driver.find_element(locator_error_message.by, locator_error_message.value) # Сообщение об ошибке авторизации


def test_auth_by_valid_phone_and_pass(web_browser):
    """ Позитивная проверка. Ввод корректных телефона и пароля"""
    driver = web_browser

    driver.get(base_url)     # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_phone = driver.find_element(locator_tab_phone.by, locator_tab_phone.value).click()     # Ищем кнопку "Телефон" в табе, нажимаем на нее

    field_phone = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода телефона, затем вводим коректный телефон
    field_phone.send_keys(valid_phone)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(valid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    auth_passed = driver.find_element(locator_btn_logout.by, locator_btn_logout.value) # Проверка авторизации, есть кнопка "Выйти"

def test_auth_by_invalid_phone_and_pass(web_browser):
    """ Негативная проверка. Ввод некорректных телефона и пароля"""
    driver = web_browser

    driver.get(base_url)     # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_phone = driver.find_element(locator_tab_phone.by, locator_tab_phone.value).click()  # Ищем кнопку "Телефон" в табе, нажимаем на нее

    field_phone = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода телефона,затем вводим некоректный телефон
    field_phone.send_keys(invalid_phone)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(invalid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    error_message = driver.find_element(locator_error_message.by, locator_error_message.value) # Сообщение об ошибке авторизации

def test_auth_by_valid_login_and_pass(web_browser):
    """ Позитивная проверка. Ввод корректных логина и пароля"""
    driver = web_browser

    driver.get(base_url)   # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_login = driver.find_element(locator_tab_login.by, locator_tab_login.value).click()     # Ищем кнопку "Логин" в табе, нажимаем на нее

    field_login = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода логина, затем вводим коректный логин
    field_login.send_keys(valid_login)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(valid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    auth_passed = driver.find_element(locator_btn_logout.by, locator_btn_logout.value)  # Проверка авторизациии, есть кнопка "Выйти"


def test_auth_by_invalid_login_and_pass(web_browser):
    """ Негативная проверка. Ввод некорректных логина и пароля"""
    driver = web_browser

    driver.get(base_url)     # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_login = driver.find_element(locator_tab_login.by, locator_tab_login.value).click()     # Ищем кнопку "Логин" в табе, нажимаем на нее

    field_login = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода логина,затем вводим некоректный логина
    field_login.send_keys(invalid_login)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(invalid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    error_message = driver.find_element(locator_error_message.by, locator_error_message.value) # Сообщение об ошибке авторизации

def test_auth_by_valid_perconal_account_and_pass(web_browser):
    """ Позитивная проверка. Ввод корректных лицевого счета и пароля"""
    driver = web_browser

    driver.get(base_url)   # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_account = driver.find_element(locator_tab_personal_acc.by, locator_tab_personal_acc.value).click()     # Ищем кнопку "Лицевой счет" в табе, нажимаем на нее

    field_account = driver.find_element(locator_field_username.by, locator_field_username.value)     # Ищем поле ввода лицевого счета, затем вводим коректный ЛС
    field_account.send_keys(valid_pers_acc)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)     # То же самое для поля с паролем
    field_pass.send_keys(valid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_tab_login.value)     # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    auth_passed = driver.find_element(locator_btn_logout.by, locator_btn_logout.value)  # Проверка авторизациии, есть кнопка "Выйти"


def test_auth_by_invalid_personal_account_and_pass(web_browser):
    """ Негативная проверка. Ввод некорректных лицевого счета и пароля"""
    driver = web_browser

    driver.get(base_url)  # Открыть исходную страницу:
    time.sleep(5)  # небольшая задержка

    btn_account = driver.find_element(locator_tab_personal_acc.by, locator_tab_personal_acc.value).click()  # Ищем кнопку "Лицевой счет" в табе, нажимаем на нее

    field_account = driver.find_element(locator_field_username.by, locator_field_username.value)  # Ищем поле ввода лицевого счета,затем вводим некоректный лицевой счет
    field_account.send_keys(invalid_pers_acc)

    field_pass = driver.find_element(locator_field_pass.by, locator_field_pass.value)  # То же самое для поля с паролем
    field_pass.send_keys(invalid_password)

    btn_submit = driver.find_element(locator_btn_login.by, locator_btn_login.value)  # Ищем кнопку "Войти" и нажимаем на нее
    btn_submit.click()

    time.sleep(10)  # небольшая задержка

    error_message = driver.find_element(locator_error_message.by, locator_error_message.value)  # Сообщение об ошибке авторизации

