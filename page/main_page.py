from page.BasePage import BasePage


class MainPage(BasePage):

    def should_be_main_page(self):
        self.should_be_login_url()
        self.should_be_registration_url()

    def should_be_main_page_autorization(self):
        self.should_be_account_url()
        self.should_be_change_password_url()
