from page.login_page import LoginPage
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
