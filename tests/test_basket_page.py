from page.basket_page import BasketPage
from page.login_page import LoginPage
import time


def test_guest_see_basket_page(driver):         # проверка элеменов в корзине (предварительно добавив в нее товар)
    url = "http://demowebshop.tricentis.com/health"
    page = BasketPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    time.sleep(1)
    page.enter_to_basket()
    page.should_be_basket_page()
    time.sleep(1)


def test_quantity_change_recalculation(driver):         # тест на изменение количества товара в корзине
    url = "http://demowebshop.tricentis.com/health"     # (проверка перерасчета суммы после изменения количества)
    page = BasketPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    time.sleep(1)
    page.enter_to_basket()
    count = 5
    page.quantity_change(count)
    time.sleep(2)


def test_ordering(driver):        # Авторизация/добавление товара в корзину/оформление заказа/удаление адреса в профиле
    url = 'http://demowebshop.tricentis.com/login'  # (проверка сообщения о успешном оформлении товара)
    page = LoginPage(driver, url)
    page.open()
    email = 'Tokar@mail.com'
    password = '123456'
    page.authorized_user(email, password)
    url = "http://demowebshop.tricentis.com/health"
    page = BasketPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    time.sleep(1)
    page.enter_to_basket()
    city = 'Санкт-Петербург'
    address = 'Невский проспект 23'
    postal_code = '190000'
    phone = '8-900-777-55-55'
    page.ordering(city, address, postal_code, phone)
    time.sleep(1)
    page.message_success_ordering()
    page.delete_address_user()



