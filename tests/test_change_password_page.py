from page.change_password_page import ChangePasswordPage
from page.login_page import LoginPage
from page.registration_page import RegistrationPage
import pytest
import random
import time


@pytest.mark.critical_tests
def test_guest_see_change_password_page(driver):     # авторизация, затем проверка перехода на страницу смены пароля и
    url = 'http://demowebshop.tricentis.com/login'  # проверка веб элементов на странице
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.should_be_authorized_user(email, password)
    url = 'http://demowebshop.tricentis.com/customer/changepassword'
    page = ChangePasswordPage(driver, url)
    page.open()
    page.should_be_change_password()


@pytest.mark.critical_tests
def test_change_password(driver):   # регистрация нового пользователя, переход на страницу смены пароля и его изменение
    url = "http://demowebshop.tricentis.com/register"      # (проверка сообщения об успешном изменении)
    page = RegistrationPage(driver, url)
    page.open()
    count = random.randint(1, 10000)
    first_name = str("Anton") + str(count)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "@fakemail.org"
    password = 123456
    confirm_password = password
    page.register_new_user(first_name, last_name, email, password, confirm_password)
    url = "http://demowebshop.tricentis.com/customer/changepassword"
    page = ChangePasswordPage(driver, url)
    page.open()
    old_password = password
    new_password = str(time.time() + count)
    confirm_password = new_password
    page.change_password(old_password, new_password, confirm_password)
    time.sleep(2)


def test_change_incorrect_old_password(driver):         # регистрация, переход на страницу смены пароля, попытка
    url = "http://demowebshop.tricentis.com/register"  # изменения пароля, введя некорректный старый пароль.
    page = RegistrationPage(driver, url)               # (проверка появляющегося сообщения об ошибке изменения)
    page.open()
    count = random.randint(1, 10000)
    first_name = str("Anton") + str(count)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "@fakemail.org"
    password = 123456
    confirm_password = password
    page.register_new_user(first_name, last_name, email, password, confirm_password)
    url = "http://demowebshop.tricentis.com/customer/changepassword"
    page = ChangePasswordPage(driver, url)
    page.open()
    old_password = 999999
    new_password = str(time.time() + count)
    confirm_password = new_password
    page.change_incorrect_old_password(old_password, new_password, confirm_password)
    time.sleep(2)
