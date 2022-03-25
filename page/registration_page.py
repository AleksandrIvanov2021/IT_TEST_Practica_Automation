from page.BasePage import BasePage
from page.locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def should_be_registration_page(self):
        self.__should_be_registration_url()
        self.__should_be_personal_detail_form()
        self.__should_be_password_form()
        self.__should_be_gender_male_radiobutton()
        self.__should_be_gender_female_radiobutton()
        self.__should_be_first_name_field()
        self.__should_be_last_name_field()
        self.__should_be_email_field()
        self.__should_be_password_field()
        self.__should_be_conform_password_field()
        self.__should_be_register_button()

    def __should_be_registration_url(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTRATION_URL), "Login url is not presented"
        login_link = self.driver.find_element(*RegistrationPageLocators.REGISTRATION_URL)
        login_link.click()
        assert "register" in self.driver.current_url, "There is not register in url"

    def __should_be_personal_detail_form(self):
        assert self.is_element_present(*RegistrationPageLocators.PERSONAL_DETAILS_FORM), \
            "Personal Details form is not presented"

    def __should_be_password_form(self):
        assert self.is_element_present(*RegistrationPageLocators.PASSWORD_FORM), "Password field is not presented"

    def __should_be_gender_male_radiobutton(self):
        assert self.is_element_present(*RegistrationPageLocators.GENDER_MALE_RADIOBUTTON), \
            "Male radiobutton is not presented"

    def __should_be_gender_female_radiobutton(self):
        assert self.is_element_present(*RegistrationPageLocators.GENDER_FEMALE_RADIOBUTTON), \
            "Female radio is not presented"

    def __should_be_first_name_field(self):
        assert self.is_element_present(*RegistrationPageLocators.FIRST_NAME), "first name field is not presented"

    def __should_be_last_name_field(self):
        assert self.is_element_present(*RegistrationPageLocators.LAST_NAME), "last name field is not presented"

    def __should_be_email_field(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_EMAIL), "email field is not presented"

    def __should_be_password_field(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_PASSWORD_1), "password field is not presented"

    def __should_be_conform_password_field(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_PASSWORD_2), \
            "confirm password field is not presented"

    def __should_be_register_button(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTER_BUTTON), "register button is not presented"

    def __should_be_continue_button(self):
        assert self.is_element_present(*RegistrationPageLocators.CONTINUE_BUTTON), "continue button is not presented"

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
        self.__should_be_continue_button()
        button_continue = self.driver.find_element(*RegistrationPageLocators.CONTINUE_BUTTON)
        button_continue.click()

