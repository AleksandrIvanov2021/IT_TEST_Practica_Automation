from page.BasePage import BasePage
from page.locators import RegistrationPageLocators


class RegistrationPage(BasePage):

    def should_be_registration_page(self):
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

    def length_password_message(self):
        length_password_message = self.driver.find_element(*RegistrationPageLocators.LENGTH_PASSWORD_MESSAGE).text
        assert length_password_message == "The password should have at least 6 characters."

    def first_name_empty_message(self):
        first_name_message = self.driver.find_element(*RegistrationPageLocators.EMPTY_FIRST_NAME_MESSAGE).text
        assert first_name_message == "First name is required."

    def registr_new_user(self, first_name, last_name, email, password, confirm_password):
        self.click_to_radiobutton_gender_registr()
        self.filling_in_the_first_name_registr(first_name)
        self.filling_in_the_last_name_registr(last_name)
        self.filling_in_the_email_registr(email)
        self.filling_in_the_password_registr(password)
        self.filling_in_the_confirm_password_registr(confirm_password)
        self.click_to_button_registration()
        self.click_to_button_continue_registration()

    def short_password_length(self, password, confirm_password):
        self.filling_in_the_password_registr(password)
        self.filling_in_the_confirm_password_registr(confirm_password)

    def registration_with_empty_field_first_name(self, last_name, email, password, confirm_password):
        self.filling_in_the_last_name_registr(last_name)
        self.filling_in_the_email_registr(email)
        self.filling_in_the_password_registr(password)
        self.filling_in_the_confirm_password_registr(confirm_password)
        self.click_to_button_registration()



