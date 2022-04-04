from page.BasePage import BasePage
from page.locators import ChangePasswordPageLocators, MainPageLocators


class ChangePasswordPage(BasePage):
    def should_be_change_password(self):
        self.__should_be_change_password_form()
        self.__should_be_old_password_field()
        self.__should_be_new_password_field()
        self.__should_be_confirm_password_field()
        self.__should_be_change_password_button()

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

    def filling_old_password_changed(self, old_password):
        old_password_field = self.driver.find_element(*ChangePasswordPageLocators.OLD_PASSWORD)
        old_password_field.send_keys(old_password)

    def filling_new_password_changed(self, new_password):
        new_password_field = self.driver.find_element(*ChangePasswordPageLocators.NEW_PASSWORD)
        new_password_field.send_keys(new_password)

    def filling_confirm_password_changed(self, confirm_password):
        confirm_password_field = self.driver.find_element(*ChangePasswordPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_password)

    def click_to_the_change_password_button(self):
        change_password_button = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON)
        change_password_button.click()

    def checking_the_password_change_message(self):
        message = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_MESSAGE).text
        assert message == 'Password was changed', 'Error when changing password'

    def checking_the_incorrect_old_password_message(self):
        change_message = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_MESSAGE_INCORRECT).text
        assert change_message == "Old password doesn't match"

    def change_password(self, old_password, new_password, confirm_password):
        self.filling_old_password_changed(old_password)
        self.filling_new_password_changed(new_password)
        self.filling_confirm_password_changed(confirm_password)
        self.click_to_the_change_password_button()

    def change_incorrect_old_password(self, old_password, new_password, confirm_password):
        self.filling_old_password_changed(old_password)
        self.filling_new_password_changed(new_password)
        self.filling_confirm_password_changed(confirm_password)
        self.click_to_the_change_password_button()
