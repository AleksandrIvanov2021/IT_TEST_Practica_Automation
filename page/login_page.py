from page.BasePage import BasePage
from page.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.__should_be_returning_customer_form()
        self.__should_be_login_email_field()
        self.__should_be_login_password_field()
        self.__should_be_checkbox_save()
        self.__should_be_login_button()
        self.__should_be_forgot_password_link()

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

    def login_message_with_empty_fields(self):
        login_message = self.driver.find_element(*LoginPageLocators.LOGIN_MESSAGE).text
        assert login_message == "Login was unsuccessful. Please correct the errors and try again."

    def login_account_message_with_empty_fields(self):
        login_account_message = self.driver.find_element(*LoginPageLocators.LOGIN_ACCOUNT_MESSAGE).text
        assert login_account_message == "No customer account found"

    def login_message_with_incorrect_password(self):
        login_message = self.driver.find_element(*LoginPageLocators.LOGIN_MESSAGE).text
        assert login_message == "Login was unsuccessful. Please correct the errors and try again."

    def login_account_message_with_incorrect_password(self):
        login_account_message = self.driver.find_element(*LoginPageLocators.LOGIN_ACCOUNT_MESSAGE).text
        assert login_account_message == "The credentials provided are incorrect"

    def click_to_forgot_password_link(self):
        forgot_password_link = self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD)
        forgot_password_link.click()

    def filling_email_recovery_forgot_password(self, email):
        email_recovery = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_recovery.send_keys(email)

    def click_to_recovery_button_forgot_password(self):
        recovery_button = self.driver.find_element(*LoginPageLocators.RECOVERY_BUTTON)
        recovery_button.click()

    def forgot_password_message_recovery_success(self):
        message_recovery = self.driver.find_element(*LoginPageLocators.RECOVERY_MESSAGE).text
        assert message_recovery == "Email with instructions has been sent to you.", "Error recovery password"

    def forgot_password_recovery(self, email):
        self.click_to_forgot_password_link()
        self.filling_email_recovery_forgot_password(email)
        self.click_to_recovery_button_forgot_password()

    def authorization_with_incorrect_password(self, email):
        self.filling_in_the_email_autorized(email)
        self.click_to_login_button_autorized()



