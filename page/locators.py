from selenium.webdriver.common.by import By


class MainPageLocators:
    REGISTRATION_URL = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_URL = (By.CSS_SELECTOR, ".ico-login")
    ACCOUNT_LINK = (By.CSS_SELECTOR, ".header-links>ul>li>a.account")
    CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, ".list>li:nth-child(7)>a")
    PRODUCT_PAGE_BOOKS_LINK = (By.CSS_SELECTOR, ".inactive>a")
    BASKET_LINK = (By.CSS_SELECTOR, ".ico-cart>span.cart-label")


class RegistrationPageLocators:
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
    CHANGE_PASSWORD_FORM = (By.CSS_SELECTOR, ".fieldset")
    OLD_PASSWORD = (By.CSS_SELECTOR, "#OldPassword")
    NEW_PASSWORD = (By.CSS_SELECTOR, "#NewPassword")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#ConfirmNewPassword")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".button-1.change-password-button")
    CHANGE_MESSAGE = (By.CSS_SELECTOR, ".result")
    CHANGE_MESSAGE_INCORRECT = (By.CSS_SELECTOR, ".validation-summary-errors>ul>li")


class ProductPageLocators:
    BOOK_NAME_DETAIL_PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-name>h1")
    BOOK_PRICE_DETAIL_PRODUCT_PAGE = (By.CSS_SELECTOR, ".price-value-22")
    ADD_BUTTON_DETAIL_PRODUCT_PAGE = (By.CSS_SELECTOR, "#add-to-cart-button-22[value='Add to cart']")
    ADD_BUTTON_LIST_PRODUCT_PAGE = (By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button[onclick*='22/1/1']")
    SUCCESS_MESSAGE_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".content>a")


class BasketPageLocators:
    BOOK_NAME_BASKET_PAGE = (By.CSS_SELECTOR, ".product-name")
    BOOK_PRICE_BASKET_PAGE = (By.CSS_SELECTOR, ".product-unit-price")
    COUNT_PRODUCT_FIELD = (By.CSS_SELECTOR, ".qty-input")
    TOTAL_PRICE_PRODUCT = (By.CSS_SELECTOR, ".product-subtotal")
    CHECKBOX_AGREEMENT = (By.CSS_SELECTOR, ".terms-of-service #termsofservice")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "#checkout[name='checkout']")
    ORDERING_COUNTRY = (By.CSS_SELECTOR, "#BillingNewAddress_CountryId.valid")
    ORDERING_CITY = (By.CSS_SELECTOR, "#BillingNewAddress_City ")
    ORDERING_ADDRESS = (By.CSS_SELECTOR, "#BillingNewAddress_Address1")
    ORDERING_POSTAL_CODE = (By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode")
    ORDERING_PHONE = (By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber")
    ORDERING_BUTTON_CONTINUE = (By.CSS_SELECTOR, "#billing-buttons-container>input")


