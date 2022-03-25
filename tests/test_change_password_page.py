from page.change_password_page import ChangePasswordPage
from page.login_page import LoginPage


def test_guest_see_registration_page(driver):        # авторизация, затем проверка перехода на страницу смены пароля и
    link = 'http://demowebshop.tricentis.com/login'  # проверка веб элементов на странице
    page = LoginPage(driver, link)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.should_be_authorized_user(email, password)
    link = 'http://demowebshop.tricentis.com/'
    page = ChangePasswordPage(driver, link)
    page.open()
    page.should_be_change_password()


