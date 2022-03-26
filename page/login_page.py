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
        self.__should_be_forgot_password_link()

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

    def __should_be_forgot_password_link(self):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "Forgot password link is not presented"

    def forgot_password_recovery(self, email):
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD), "Forgot password link is not presented"
        forgot_password_link = self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD)
        forgot_password_link.click()
        email_recovery = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_recovery.send_keys(email)
        recovery_button = self.driver.find_element(*LoginPageLocators.RECOVERY_BUTTON)
        recovery_button.click()
        message_recovery = self.driver.find_element(*LoginPageLocators.RECOVERY_MESSAGE).text
        assert message_recovery == "Email with instructions has been sent to you.", "Error recovery password"



