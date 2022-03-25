from page.registration_page import RegistrationPage
import random
import time


def test_guest_see_registration_page(driver):               # проверка перехода на страницу регистрации и веб-элементов
    link = "http://demowebshop.tricentis.com/"
    page = RegistrationPage(driver, link)
    page.open()
    page.should_be_registration_page()


def test_registration_new_user(driver):                     # регистрация нового пользователя c авторизацией на сайте
    link = "http://demowebshop.tricentis.com/register"
    page = RegistrationPage(driver, link)
    page.open()
    count = random.randint(1, 100)
    first_name = str("Anton") + str(count)
    last_name = str("Arnoldov") + str(count)
    email = str(time.time()) + "@fakemail.org"
    password = str(time.time() + count)
    confirm_password = password
    page.register_new_user(first_name, last_name, email, password, confirm_password)
    time.sleep(3)


