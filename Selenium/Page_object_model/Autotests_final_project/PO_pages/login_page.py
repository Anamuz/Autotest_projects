from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
        assert "login" in browser.current_url, 'Excpected login link'

    def should_be_login_form(self, browser):
        assert self.is_element_present(*LoginPageLocators.login_form), 'Excpected login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), 'Excpected register form'

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "qwerty123"
        reg_mail = self.browser.find_element(*RegistrationLocators.e_mail)
        reg_mail.send_keys(email)
        reg_pas1 = self.browser.find_element(*RegistrationLocators.password_1)
        reg_pas1.send_keys(password)
        reg_pas2 = self.browser.find_element(*RegistrationLocators.password_2)
        reg_pas2.send_keys(password)
        self.browser.find_element(*RegistrationLocators.reg_button).click()
