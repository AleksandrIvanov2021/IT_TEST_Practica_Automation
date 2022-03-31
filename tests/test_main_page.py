import pytest
from page.login_page import LoginPage
from page.main_page import MainPage


@pytest.mark.critical_tests
def test_guest_see_main_page(driver):  # Проверка элементов на главной странице (Registr,Login,Account,ChangePassword)
    url = "http://demowebshop.tricentis.com/"
    page = MainPage(driver, url)
    page.open()
    page.should_be_main_page()
    url = 'http://demowebshop.tricentis.com/login'
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.should_be_authorized_user(email, password)
    url = "http://demowebshop.tricentis.com/"
    page = MainPage(driver, url)
    page.open()
    page.should_be_main_page_autorization()


