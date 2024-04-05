from .base_page import BasePage
from .locators import MenuPageLocators
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage(BasePage):
    def go_to_dessert(self):
        self.browser.execute_script("window.scrollBy(0, -200)")
        action_chains = webdriver.ActionChains(self.browser)
        element = self.browser.find_element(*MenuPageLocators.menu)
        action_chains.move_to_element(element).perform()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(MenuPageLocators.menu_desserts))
        dessert_page = self.browser.find_element(*MenuPageLocators.menu_desserts)
        dessert_page.click()

    def price_filter(self):
        action_chains = webdriver.ActionChains(self.browser)
        slider = self.browser.find_element(*MenuPageLocators.right_slider)
        action_chains\
            .click_and_hold(slider)\
            .move_by_offset(-150, 0)\
            .release()\
            .perform()
        button = self.browser.find_element(*MenuPageLocators.filter_button)
        button.click()
        assert self.check_price(), "Expected prices to be equal"

    def check_price(self):
        budget = 135
        elements = self.browser.find_elements(*MenuPageLocators.dessert_price)
        for price in elements:
            product_price = price.text
            quantity = ''

            for number in product_price:
                if ('0' <= number <= '9'):
                    quantity += number

            if quantity:
                checkprice = int(quantity) // 100
                if checkprice > budget:
                    return False
        return True

    def choose_dessert(self):
        button = self.browser.find_element(*MenuPageLocators.dessert_button)
        button.click()
