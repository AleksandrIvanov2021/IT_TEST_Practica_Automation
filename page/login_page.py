from page.BasePage import BasePage
from page.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.__should_be_login_url()
        self.__should_be_returning_customer_form()
        self.__should_be_login_email_field()
        self.__should_be_login_password_field()
        self.__should_be_checkbox_save()
        self.__should_be_login_button()

    def __should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login url is not presented"
        login_link = self.driver.find_element(*LoginPageLocators.LOGIN_URL)
        login_link.click()
        assert "login" in self.driver.current_url, "There is not login in url"

    def __should_be_returning_customer_form(self):
        assert self.is_element_present(*LoginPageLocators.RETURNING_CUSTOMER_FORM), "Form is not presented"

    def __should_be_login_email_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Email field is not presented"

    def __should_be_login_password_field(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field is not presented"

    def __should_be_checkbox_save(self):
        assert self.is_element_present(*LoginPageLocators.CHECKBOX_SAVE), "Checkbox is not presented"

    def __should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_authorized_user(self, email, password):
        email_field = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_field.send_keys(password)
        checkbox = self.driver.find_element(*LoginPageLocators.CHECKBOX_SAVE)
        checkbox.click()
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
