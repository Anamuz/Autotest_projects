import uuid
from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegisterPage(BasePage):
    def register(self):
        self.browser.find_element(*RegistrationPageLocators.my_acc).click()
        self.browser.find_element(*RegistrationPageLocators.go_to_registration).click()
        random_username = 'Username' + str(uuid.uuid4().hex)[:3]
        username = self.browser.find_element(*RegistrationPageLocators.username)
        username.send_keys(random_username)
        email = self.browser.find_element(*RegistrationPageLocators.email)
        email.send_keys(f'{random_username}@mail.com')
        password = self.browser.find_element(*RegistrationPageLocators.password)
        password.send_keys('qwerty123')
        self.browser.find_element(*RegistrationPageLocators.register_button).click()

    def return_to_main_page(self):
        self.browser.find_element(*RegistrationPageLocators.return_to_main).click()


'''
    def register(self):
        self.browser.find_element(*RegistrationPageLocators.my_acc).click()
        username = self.browser.find_element(*RegistrationPageLocators.username)
        username.send_keys('Username_1')
        email = self.browser.find_element(*RegistrationPageLocators.email)
        email.send_keys('Username_1@email.com')
        password = self.browser.find_element(*RegistrationPageLocators.password)
        password.send_keys('qwerty123')
        self.browser.find_element(*RegistrationPageLocators.register_button).click()
'''
