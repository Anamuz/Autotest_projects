from .base_page import BasePage
from .locators import BonusPageLocators
from selenium.common.exceptions import NoAlertPresentException


class BonusPage(BasePage):
    def go_bonus_page(self):
        bonus = self.browser.find_element(*BonusPageLocators.bonus_page)
        bonus.click()

    def should_be_bonus_page(self):
        bonus_page_link = 'https://pizzeria.skillbox.cc/bonus/'
        get_url = self.browser.current_url
        assert bonus_page_link == get_url, "Bonus page expected to be opened"

    def enter_details(self):
        username = self.browser.find_element(*BonusPageLocators.name)
        username.send_keys('Username')
        user_phone = self.browser.find_element(*BonusPageLocators.phone)
        user_phone.send_keys('+79876543210')
        self.browser.find_element(*BonusPageLocators.order_card).click()

    def alert_message(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Expected to be alert message: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No alert presented")

    def card_issued_message(self):
        expected_text = 'Ваша карта оформлена!'
        actual_text = self.browser.find_element(*BonusPageLocators.success_text).text
        assert expected_text == actual_text, \
            f"Expected to be alert message: {expected_text}, after successful operation"

    def enter_invalid_details(self):
        self.enter_invalid_phone()
        self.enter_invalid_name()

    def enter_invalid_phone(self):
        user_phone = self.browser.find_element(*BonusPageLocators.phone)
        user_phone.send_keys('qwerty')
        self.should_be_validation_message_phone()

    def enter_invalid_name(self):
        user_name = self.browser.find_element(*BonusPageLocators.name)
        user_name.clear()
        self.browser.find_element(*BonusPageLocators.order_card).click()
        self.should_be_validation_message_name()

    def should_be_validation_message_phone(self):
        validation_message = 'Введен неверный формат телефона'
        message = self.browser.find_element(*BonusPageLocators.validation_message).text
        assert validation_message in message, f'Expected {validation_message} message for phone input'

    def should_be_validation_message_name(self):
        validation_message = 'Поле "Имя" обязательно для заполнения'
        message = self.browser.find_element(*BonusPageLocators.validation_message).text
        assert validation_message in message, f'Expected {validation_message} message for name input'
