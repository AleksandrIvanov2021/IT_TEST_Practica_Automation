import pytest
from page.login_page import LoginPage
import random
import time


@pytest.mark.critical_tests
def test_guest_see_login_page(driver):                # проверка перехода на страницу авторизации и веб-элементов
    url = "http://demowebshop.tricentis.com/login"
    page = LoginPage(driver, url)
    page.open()
    page.should_be_login_page()


@pytest.mark.critical_tests
def test_authorized_user(driver):                    # авторизация существующего пользователя
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.should_be_authorized_user(email, password)
    time.sleep(2)


@pytest.mark.xfail
def test_authorized_incorrect(driver):                # авторизация несуществующего пользователя
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    count = random.randint(1, 10000)
    email = str(count) + '@mail.com'
    password = str(count) + '9124723785623'
    page.should_be_authorized_user(email, password)
    time.sleep(2)


def test_password_recovery(driver):                    # проверка восстановления пароля (забыли пароль?)
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    page.forgot_password_recovery(email)
    time.sleep(2)


def test_authorization_with_empty_fields(driver):      # авторизация с пустыми полями (проверка появлющихся сообщений)
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    page.authorization_with_empty_fields()
    time.sleep(2)


def test_authorization_with_incorrect_password(driver):  # авторизация с некорректным паролем(проверка появл. сообщений)
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    page.authorization_with_incorrect_password(email)
    time.sleep(2)

