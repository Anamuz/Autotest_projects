from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def choose_pizza(self):
        # WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(BasePageLocators.first_pizza_name))
        # do not work, as text do not copy properly
        time.sleep(3)
        first_pizza_title = self.browser.find_element(*BasePageLocators.first_pizza_name).text
        self.browser.find_element(*BasePageLocators.first_product_button).click()
        return first_pizza_title

    def should_be_slider(self):
        assert self.is_element_present(*BasePageLocators.slider), "Slider is not presented"

    def should_be_cart_button(self):
        assert self.is_element_present(*BasePageLocators.cart_button), "Button 'В корзину' is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def to_cart(self):
        button = self.browser.find_element(*BasePageLocators.cart_button)
        button.click()

    def run_through_left(self):
        action = webdriver.ActionChains(self.browser)
        slider_button = self.browser.find_element(*BasePageLocators.left_slider_button)
        action.move_to_element(slider_button)
        slider_button.click()

    def run_through_right(self):
        action = webdriver.ActionChains(self.browser)
        slider_button = self.browser.find_element(*BasePageLocators.right_slider_button)
        action.move_to_element(slider_button)
        slider_button.click()

    def add_second_pizza(self):
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(BasePageLocators.another_pizza_name))
        second_pizza_title = self.browser.find_element(*BasePageLocators.another_pizza_name).text
        self.browser.find_element(*BasePageLocators.another_pizza_button).click()
        return second_pizza_title

    def open_pizza_page(self):
        pizza_title = self.browser.find_element(*BasePageLocators.third_pizza_name).text
        self.browser.find_element(*BasePageLocators.third_pizza_name).click()
        result_title = self.browser.find_element(*ProductPageLocators.pizza_title).text
        assert pizza_title.lower() in result_title.lower(), f'Expected text: {pizza_title}, but got {result_title}'

    def add_products(self):
        self.browser.implicitly_wait(20)
        action = webdriver.ActionChains(self.browser)
        add_first = self.browser.find_element(*BasePageLocators.first_product)
        action.move_to_element(add_first)
        self.browser.find_element(*BasePageLocators.first_product_button).click()
        add_second = self.browser.find_element(*BasePageLocators.second_product)
        action.move_to_element(add_second)
        self.browser.find_element(*BasePageLocators.second_product_button).click()
        time.sleep(3)
        # added a sleep delay because the server couldn't keep up with the rapid actions being performed

    def turn_text_into_int(self, overall):
        price_text = overall.replace('₽', '').replace(',', '').strip()
        price = int(price_text)
        price //= 100
        return price
