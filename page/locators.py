from selenium.webdriver.common.by import By


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
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".button-1.register-continue-button")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, ".ico-login")
    RETURNING_CUSTOMER_FORM = (By.CSS_SELECTOR, ".returning-wrapper")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#Email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#Password")
    CHECKBOX_SAVE = (By.CSS_SELECTOR, "#RememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button-1.login-button")


class ChangePasswordPageLocators:
    ACCOUNT_LINK = (By.CSS_SELECTOR, ".header-links>ul>li>a.account")
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, ".list>li:nth-child(7)>a")
    CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, ".fieldset")
    OLD_PASSWORD = (By.CSS_SELECTOR, "#OldPassword")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#NewPassword")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".button-1.change-password-button")


