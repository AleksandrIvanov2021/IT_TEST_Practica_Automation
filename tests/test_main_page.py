import pytest
from page.login_page import LoginPage
from page.main_page import MainPage


@pytest.mark.critical_tests
def test_guest_see_main_page(driver):  # Проверка элементов на главной странице (Registr,Login,Books link)
    url = "http://demowebshop.tricentis.com/"
    page = MainPage(driver, url)
    page.open()
    page.should_be_main_page()


@pytest.mark.critical_tests             # Авторизация, затем проверка элементов (Account,ChangePassword)
def test_guest_see_main_page_autorized(driver):
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.authorized_user(email, password)
    url = "http://demowebshop.tricentis.com/"
    page = MainPage(driver, url)
    page.open()
    page.should_be_main_page_autorization()


