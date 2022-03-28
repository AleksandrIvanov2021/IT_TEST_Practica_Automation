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
    LENGTH_PASSWORD_MESSAGE = (By.CSS_SELECTOR, ".field-validation-error>[for='Password']")
    EMPTY_FIRST_NAME_MESSAGE = (By.CSS_SELECTOR, ".field-validation-error>[for='FirstName']")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, ".ico-login")
    RETURNING_CUSTOMER_FORM = (By.CSS_SELECTOR, ".returning-wrapper")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#Email")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#Password")
    CHECKBOX_SAVE = (By.CSS_SELECTOR, "#RememberMe")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button-1.login-button")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, ".inputs.reversed>span>a")
    RECOVERY_BUTTON = (By.CSS_SELECTOR, ".button-1.password-recovery-button")
    RECOVERY_MESSAGE = (By.CSS_SELECTOR, ".page-body>.result")
    LOGIN_MESSAGE = (By.CSS_SELECTOR, ".validation-summary-errors>span")
    LOGIN_ACCOUNT_MESSAGE = (By.CSS_SELECTOR, ".validation-summary-errors>ul>li")


class ChangePasswordPageLocators:
    ACCOUNT_LINK = (By.CSS_SELECTOR, ".header-links>ul>li>a.account")
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, ".list>li:nth-child(7)>a")
    CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, ".fieldset")
    OLD_PASSWORD = (By.CSS_SELECTOR, "#OldPassword")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#NewPassword")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".button-1.change-password-button")
    CHANGE_MESSAGE = (By.CSS_SELECTOR, ".result")
    CHANGE_MESSAGE_INCORRECT = (By.CSS_SELECTOR, ".validation-summary-errors>ul>li")
