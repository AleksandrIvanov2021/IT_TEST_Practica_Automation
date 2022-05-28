from page.product_page import ProductPage
import time


def test_guest_see_product_page(driver):      # проверка элементов на странице деталей товара и странице списка товара
    url = "http://demowebshop.tricentis.com/health"
    page = ProductPage(driver, url)
    page.open()
    page.should_be_product_detail_page()
    url = "http://demowebshop.tricentis.com/books"
    page = ProductPage(driver, url)
    page.open()
    time.sleep(2)
    page.should_be_add_button_list_product_page()


def test_add_to_basket_in_detail_product_page(driver):  # добавление товара в корзину со страницы деталей товара
    url = "http://demowebshop.tricentis.com/health"     # (проверка сообщения об успешном добавлении товара в корзину)
    page = ProductPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    page.message_add_product_to_basket()
    time.sleep(2)


def test_add_to_basket_in_list_product_page(driver):    # добавление товара в корзину со страницы списка товаров
    url = "http://demowebshop.tricentis.com/books"     # (проверка сообщения об успешном добавлении товара в корзину)
    page = ProductPage(driver, url)
    page.open()
    page.add_to_basket_list_product_page()
    page.message_add_product_to_basket()
    time.sleep(2)


def test_checking_name_the_added_item(driver):   # проверка соответствия названия добавляемого товара и товара в корзине
    url = "http://demowebshop.tricentis.com/health"
    page = ProductPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    time.sleep(1)
    page.should_be_book_name()
    time.sleep(1)


def test_checking_price_the_added_item(driver):   # проверка соответствия цены добавляемого товара и цены в корзине
    url = "http://demowebshop.tricentis.com/health"
    page = ProductPage(driver, url)
    page.open()
    page.add_to_basket_detail_product_page()
    time.sleep(1)
    page.should_be_book_price()
    time.sleep(1)
