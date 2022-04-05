from page.BasePage import BasePage
from page.locators import ProductPageLocators, BasketPageLocators, MainPageLocators


class ProductPage(BasePage):

    def should_be_product_detail_page(self):
        self.__should_be_book_name_detail_page()
        self.__should_be_book_price_detail_page()
        self.__should_be_add_button_detail_page()

    def __should_be_book_name_detail_page(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME_DETAIL_PRODUCT_PAGE), "Book name is not present"

    def __should_be_book_price_detail_page(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE_DETAIL_PRODUCT_PAGE), "Book price is not present"

    def __should_be_add_button_detail_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON_DETAIL_PRODUCT_PAGE), "Add button is not present"

    def should_be_add_button_list_product_page(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON_LIST_PRODUCT_PAGE), "Add button is not present"

    def message_add_product_to_basket(self):
        assert self.driver.find_element(*ProductPageLocators.SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET)

    def should_be_book_name(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME_DETAIL_PRODUCT_PAGE).text
        self.driver.find_element(*MainPageLocators.BASKET_LINK).click()
        book_basket_name = self.driver.find_element(*BasketPageLocators.BOOK_NAME_BASKET_PAGE).text
        assert book_name == book_basket_name, "Name is not same"

    def should_be_book_price(self):
        book_price = self.driver.find_element(*ProductPageLocators.BOOK_PRICE_DETAIL_PRODUCT_PAGE).text
        self.driver.find_element(*MainPageLocators.BASKET_LINK).click()
        book_basket_price = self.driver.find_element(*BasketPageLocators.BOOK_PRICE_BASKET_PAGE).text
        assert book_price == book_basket_price, "Price is not same"
