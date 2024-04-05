from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_additional_options(self):
        assert self.is_element_present(*ProductPageLocators.additional), "Additional options are not presented"

    def add_additional_options(self):
        select = self.browser.find_element(*ProductPageLocators.option)
        select.click()
        selection = select.text
        button = self.browser.find_element(*ProductPageLocators.cart)
        button.click()
        third_pizza_title = self.browser.find_element(*ProductPageLocators.pizza_title).text
        return third_pizza_title, selection
