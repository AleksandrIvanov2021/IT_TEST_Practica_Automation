from page.registration_page import RegistrationPage
import pytest
import random
import time


@pytest.mark.critical_tests
def test_guest_see_registration_page(driver):               # проверка перехода на страницу регистрации и веб-элементов
    url = "http://demowebshop.tricentis.com/register"
    page = RegistrationPage(driver, url)
    page.open()
    page.should_be_registration_page()


@pytest.mark.critical_tests
def test_registration_new_user(driver):                     # регистрация нового пользователя c авторизацией на сайте
    url = "http://demowebshop.tricentis.com/register"         # (проверка аккаунта на вход)
    page = RegistrationPage(driver, url)
    page.open()
    count = random.randint(1, 10000)
    first_name = str("Anton") + str(count)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time() + count)
    confirm_password = password
    page.registr_new_user(first_name, last_name, email, password,confirm_password)
    page.should_be_account_link()
    time.sleep(3)


@pytest.mark.xfail
def test_registration_incorrect_email(driver):               # регистрация нового пользователя с некорректным email
    url = "http://demowebshop.tricentis.com/register"        # (проверка, что вход неосуществлен)
    page = RegistrationPage(driver, url)
    page.open()
    count = random.randint(1, 10000)
    first_name = str("Anton") + str(count)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "yandex.baton"
    password = str(time.time() + count)
    confirm_password = password
    page.registr_new_user(first_name, last_name, email, password, confirm_password)
    page.should_be_account_link()
    time.sleep(3)


def test_short_password_length(driver):                      # проверка поля пароля на появление предупреждения при
    url = "http://demowebshop.tricentis.com/register"       # вводе меньшего кол-ва необх. символов (минимальное - 6)
    page = RegistrationPage(driver, url)
    page.open()
    password = '123'
    confirm_password = password
    page.short_password_length(password, confirm_password)
    page.length_password_message()
    time.sleep(2)


def test_registration_with_empty_field_first_name(driver):   # регистрация с пустым полем 'FIRST NAME'
    url = "http://demowebshop.tricentis.com/register"       # (проверка предупреждения о незаполненном поле)
    page = RegistrationPage(driver, url)
    page.open()
    count = random.randint(1, 10000)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time() + count)
    confirm_password = password
    page.registration_with_empty_field_first_name(last_name, email, password, confirm_password)
    page.first_name_empty_message()
    time.sleep(2)
