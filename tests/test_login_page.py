import pytest
from page.login_page import LoginPage
import random
import time


def test_guest_see_login_page(driver):                # проверка перехода на страницу авторизации и веб-элементов
    link = "http://demowebshop.tricentis.com/"
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_page()


def test_authorized_user(driver):                    # авторизация существующего пользователя
    link = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, link)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.should_be_authorized_user(email, password)
    time.sleep(3)


@pytest.mark.xfail
def test_authorized_incorrect(driver):                # авторизация несуществующего пользователя
    link = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, link)
    page.open()
    count = random.randint(1, 10000)
    email = str(count) + '@mail.com'
    password = str(count) + '9124723785623'
    page.should_be_authorized_user(email, password)
    time.sleep(2)


def test_password_recovery(driver):                    # проверка восстановления пароля (забыли пароль?)
    link = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, link)
    page.open()
    email = 'Tokar@mail.com'
    page.forgot_password_recovery(email)
    time.sleep(2)
