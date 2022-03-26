from selenium.common.exceptions import NoSuchElementException
from page.locators import LoginPageLocators, RegistrationPageLocators, ChangePasswordPageLocators


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

    def should_be_authorized_user(self, email, password):
        email_field = self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        password_field.send_keys(password)
        checkbox = self.driver.find_element(*LoginPageLocators.CHECKBOX_SAVE)
        checkbox.click()
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        assert self.is_element_present(*ChangePasswordPageLocators.ACCOUNT_LINK), "Authorization failed"

    def register_new_user(self, first_name, last_name, email, password, confirm_password):
        radiobutton_gender_field = self.driver.find_element(*RegistrationPageLocators.GENDER_FEMALE_RADIOBUTTON)
        radiobutton_gender_field.click()
        first_name_field = self.driver.find_element(*RegistrationPageLocators.FIRST_NAME)
        first_name_field.send_keys(first_name)
        last_name_field = self.driver.find_element(*RegistrationPageLocators.LAST_NAME)
        last_name_field.send_keys(last_name)
        email_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_EMAIL)
        email_field.send_keys(email)
        password_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_1)
        password_field.send_keys(password)
        confirm_password_field = self.driver.find_element(*RegistrationPageLocators.REGISTER_PASSWORD_2)
        confirm_password_field.send_keys(confirm_password)
        button_registration_submit = self.driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        button_registration_submit.click()
        assert self.is_element_present(*RegistrationPageLocators.CONTINUE_BUTTON), "continue button is not presented"
        button_continue = self.driver.find_element(*RegistrationPageLocators.CONTINUE_BUTTON)
        button_continue.click()
        assert self.is_element_present(*ChangePasswordPageLocators.ACCOUNT_LINK), "Registration failed"

    def change_password(self, old_password, new_password, confirm_password):
        account_link = self.driver.find_element(*ChangePasswordPageLocators.ACCOUNT_LINK)
        account_link.click()
        change_password_link = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_LINK)
        change_password_link.click()
        old_password_field = self.driver.find_element(*ChangePasswordPageLocators.OLD_PASSWORD)
        old_password_field.send_keys(old_password)
        new_password_field = self.driver.find_element(*ChangePasswordPageLocators.NEW_PASSWORD)
        new_password_field.send_keys(new_password)
        confirm_password_field = self.driver.find_element(*ChangePasswordPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_password)
        change_password_button = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_PASSWORD_BUTTON)
        change_password_button.click()
        message = self.driver.find_element(*ChangePasswordPageLocators.CHANGE_MESSAGE).text
        assert message == 'Password was changed', 'Error when changing password'


