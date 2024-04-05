from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_logged(self):
        self.browser.find_element(*LoginPageLocators.to_myacc).click()
        self.browser.find_element(*LoginPageLocators.edit).click()
        email_detail = self.browser.find_element(*LoginPageLocators.email)
        email_value = email_detail.get_attribute('value')
        assert self.is_element_present(*LoginPageLocators.myacc_content), \
            "MyAccount content is not presented, user is not logged"
        return email_value
