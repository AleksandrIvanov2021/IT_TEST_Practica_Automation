from selenium.webdriver.common.by import By


class BasePageLocators:
    REGISTR_LINK = (By.CSS_SELECTOR, ".ico-register")


class RegistrationPageLocators:
    REGISTRATION_URL = (By.CSS_SELECTOR, ".ico-register")
    PERSONAL_DETAILS_FORM = (By.CSS_SELECTOR, ".fieldset:nth-child(2)")
    PASSWORD_FORM = (By.CSS_SELECTOR, ".fieldset:nth-child(3)")
    GENDER_MALE_RADIOBUTTON = (By.CSS_SELECTOR, "#gender-male")
    GENDER_FEMALE_RADIOBUTTON = (By.CSS_SELECTOR, "#gender-female")
    FIRST_NAME = (By.CSS_SELECTOR, "#FirstName")
    LAST_NAME = (By.CSS_SELECTOR, "#LastName")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#Email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#Password")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register-button")
