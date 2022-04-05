from page.BasePage import BasePage
from page.locators import BasketPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.__should_be_book_name_basket_page()
        self.__should_be_book_price_basket_page()
        self.__should_be_count_product_field()
        self.__should_be_total_price_product()
        self.__should_be_checkbox_agreement()
        self.__should_be_button_checkout()

    def __should_be_book_name_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BOOK_NAME_BASKET_PAGE), "Book name is not present"

    def __should_be_book_price_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.BOOK_PRICE_BASKET_PAGE), "Book price is not present"

    def __should_be_count_product_field(self):
        assert self.is_element_present(*BasketPageLocators.COUNT_PRODUCT_FIELD), "Count product field is not present"

    def __should_be_total_price_product(self):
        assert self.is_element_present(*BasketPageLocators.TOTAL_PRICE_PRODUCT), "Total price is not present"

    def __should_be_checkbox_agreement(self):
        assert self.is_element_present(*BasketPageLocators.CHECKBOX_AGREEMENT), "Checkbox agreement is not present"

    def __should_be_button_checkout(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON_CHECKOUT), "Button checkout is not present"

    def quantity_change(self, count):
        total_sum = self.driver.find_element(*BasketPageLocators.TOTAL_PRICE_PRODUCT).text
        count_field = self.driver.find_element(*BasketPageLocators.COUNT_PRODUCT_FIELD)
        count_field.clear()
        count_field.send_keys(count, Keys.ENTER)
        total_sum_2 = self.driver.find_element(*BasketPageLocators.TOTAL_PRICE_PRODUCT).text
        assert float(total_sum) * count == float(total_sum_2), "Recalculation failed"

    def click_to_checkbox_agreement_ordering(self):
        checkbox = self.driver.find_element(*BasketPageLocators.CHECKBOX_AGREEMENT)
        checkbox.click()

    def click_to_button_checkout_ordering(self):
        checkout_button = self.driver.find_element(*BasketPageLocators.BUTTON_CHECKOUT)
        checkout_button.click()

    # def drop_down_country_ordering(self):
    #     element = self.driver.find_element(*BasketPageLocators.ORDERING_COUNTRY)
    #     drop_dawn_country = Select(element)
    #     drop_dawn_country.select_by_value("66")

    def filling_in_the_city_ordering(self, city):
        field_city = self.driver.find_element(*BasketPageLocators.ORDERING_CITY)
        field_city.send_keys(city)

    def filling_in_the_address_ordering(self, address):
        field_address = self.driver.find_element(*BasketPageLocators.ORDERING_ADDRESS)
        field_address.send_keys(address)

    def filling_in_the_postal_code_ordering(self, postal_code):
        field_postal_code = self.driver.find_element(*BasketPageLocators.ORDERING_POSTAL_CODE)
        field_postal_code.send_keys(postal_code)

    def filling_in_the_phone_ordering(self, phone):
        field_phone = self.driver.find_element(*BasketPageLocators.ORDERING_PHONE)
        field_phone.send_keys(phone)

    def click_to_the_button_continue_ordering(self):
        button_continue = self.driver.find_element(*BasketPageLocators.ORDERING_BUTTON_CONTINUE)
        button_continue.click()

    def ordering(self, city, address, postal_code, phone):
        self.click_to_checkbox_agreement_ordering()
        self.click_to_button_checkout_ordering()
       # self.drop_down_country_ordering()
        self.filling_in_the_city_ordering(city)
        self.filling_in_the_address_ordering(address)
        self.filling_in_the_postal_code_ordering(postal_code)
        self.filling_in_the_phone_ordering(phone)
        self.click_to_the_button_continue_ordering()






