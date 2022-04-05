from selenium.common.exceptions import NoSuchElementException
from page.locators import LoginPageLocators, RegistrationPageLocators, MainPageLocators, ProductPageLocators


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_registration_url(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_URL), "Login url is not presented"
        login_link = self.driver.find_element(*MainPageLocators.REGISTRATION_URL)
        login_link.click()
        assert "register" in self.driver.current_url, "There is not register in url"

    def should_be_login_url(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.driver.find_element(*MainPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.driver.current_url, "There is not login in url"

    def should_be_account_url(self):
        assert self.is_element_present(*MainPageLocators.ACCOUNT_LINK), "Account url is not presented"
        login_link = self.driver.find_element(*MainPageLocators.ACCOUNT_LINK)
        login_link.click()
        assert "customer/info" in self.driver.current_url, "There is not account in url"

    def should_be_change_password_url(self):
        assert self.is_element_present(*MainPageLocators.CHANGE_PASSWORD_LINK), \
            "Change password url is not presented"
        login_link2 = self.driver.find_element(*MainPageLocators.CHANGE_PASSWORD_LINK)
        login_link2.click()
        assert "customer/changepassword" in self.driver.current_url, "There is not change password in url"

    def should_be_product_page_books_link(self):
        assert self.is_element_present(*MainPageLocators.PRODUCT_PAGE_BOOKS_LINK), \
            "Books link url is not presented"
        books_link = self.driver.find_element(*MainPageLocators.PRODUCT_PAGE_BOOKS_LINK)
        books_link.click()
        assert "/books" in self.driver.current_url, "There is not books link in url"

    def should_be_basket_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_LINK), "Basket link is not presented"

    def enter_to_basket(self):
        basket_link = self.driver.find_element(*MainPageLocators.BASKET_LINK)
        basket_link.click()

    def add_to_basket_detail_product_page(self):
        button_add = self.driver.find_element(*ProductPageLocators.ADD_BUTTON_DETAIL_PRODUCT_PAGE)
        button_add.click()

    def add_to_basket_list_product_page(self):
        button_add_to_list_product = self.driver.find_element(*ProductPageLocators.ADD_BUTTON_LIST_PRODUCT_PAGE)
        button_add_to_list_product.click()

    def should_be_account_link(self):
        assert self.is_element_present(*MainPageLocators.ACCOUNT_LINK), "Account link not found"

    def filling_in_the_email_autorized(self, email):
        email_field = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)

    def filling_in_the_password_autorized(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_field.send_keys(password)

    def click_to_checkbox_autorized(self):
        checkbox = self.driver.find_element(*LoginPageLocators.CHECKBOX_SAVE)
        checkbox.click()

    def click_to_login_button_autorized(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def authorized_user(self, email, password):
        self.filling_in_the_email_autorized(email)
        self.filling_in_the_password_autorized(password)
        self.click_to_checkbox_autorized()
        self.click_to_login_button_autorized()

    def click_to_radiobutton_gender_registr(self):
        radiobutton_gender_field = self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE_RADIOBUTTON)
        radiobutton_gender_field.click()

    def filling_in_the_first_name_registr(self, first_name):
        first_name_field = self.driver.find_element(*RegistrationPageLocators.FIRST_NAME)
        first_name_field.send_keys(first_name)

    def filling_in_the_last_name_registr(self, last_name):
        last_name_field = self.driver.find_element(*RegistrationPageLocators.LAST_NAME)
        last_name_field.send_keys(last_name)

    def filling_in_the_email_registr(self, email):
        email_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)

    def filling_in_the_password_registr(self, password):
        password_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_1)
        password_field.send_keys(password)

    def filling_in_the_confirm_password_registr(self, confirm_password):
        confirm_password_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_2)
        confirm_password_field.send_keys(confirm_password)

    def click_to_button_registration(self):
        button_registration_submit = self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        button_registration_submit.click()

    def click_to_button_continue_registration(self):
        button_continue = self.driver.find_element(*RegistrationPageLocators.CONTINUE_BUTTON)
        button_continue.click()



