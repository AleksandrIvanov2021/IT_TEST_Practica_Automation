from page.BasePage import BasePage
from page.locators import ChangePasswordPageLocators


class ChangePasswordPage(BasePage):
    def should_be_change_password(self):
        self.__should_be_account_url()
        self.__should_be_change_password_url()
        self.__should_be_change_password_form()
        self. __should_be_old_password_field()
        self.__should_be_new_password_field()
        self.__should_be_confirm_password_field()
        self.__should_be_change_password_button()

    def __should_be_account_url(self):
        assert self.is_element_present(*ChangePasswordPageLocators.ACCOUNT_LINK), "Account url is not presented"
        login_link = self.driver.find_element(*ChangePasswordPageLocators.ACCOUNT_LINK)
        login_link.click()
        assert "customer/info" in self.driver.current_url, "There is not account in url"

    def __should_be_change_password_url(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_LINK), \
            "Change password url is not presented"
        login_link2 = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_LINK)
        login_link2.click()
        assert "customer/changepassword" in self.driver.current_url, "There is not change password in url"

    def __should_be_change_password_form(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_FORM), "Form is not presented"

    def __should_be_old_password_field(self):
        assert self.is_element_present(*ChangePasswordPageLocators.OLD_PASSWORD), "Old password is not presented"

    def __should_be_new_password_field(self):
        assert self.is_element_present(*ChangePasswordPageLocators.NEW_PASSWORD), "New password is not presented"

    def __should_be_confirm_password_field(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CONFIRM_PASSWORD), "Confirm password is not present"

    def __should_be_change_password_button(self):
        assert self.is_element_present(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON), "Button is not presented"