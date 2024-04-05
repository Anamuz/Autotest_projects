from .base_page import BasePage
from .locators import CartPageLocators
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def go_to_cart(self):
        time.sleep(2)
        # added a sleep delay because the server couldn't keep up with the rapid actions being performed
        button = self.browser.find_element(*CartPageLocators.cart_button)
        button.click()

    def check_products(self, first_pizza, second_pizza, third_pizza):
        titles = self.browser.find_elements(*CartPageLocators.product_title)
        additional = self.browser.find_element(*CartPageLocators.product_additional).text
        selected = third_pizza[1]
        cart_product_titles = [element.text.lower() for element in titles]
        returned_titles = [title.lower() for title in [first_pizza, second_pizza, third_pizza[0]]]
        cart_product_titles = [title.replace('"', '') for title in cart_product_titles]
        returned_titles = [title.replace('«', '').replace('»', '') for title in returned_titles]
        selected_parts = selected.lower().split(' - ')[0]
        additional_parts = additional.lower().split(' ')[0]
        match_found = any(selected_part in additional_parts for selected_part in selected_parts)
        assert match_found, "Selected option does not match any additional options in the cart."
        assert all(title in cart_product_titles for title in returned_titles), \
            "Not all returned titles are present in the cart."

    def change_quantity(self):
        quantity = self.browser.find_element(*CartPageLocators.change_quantity)
        quantity.clear()
        quantity.send_keys('4')
        button = self.browser.find_element(*CartPageLocators.update_button)
        button.click()

    def delete_product(self):
        # WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(CartPageLocators.product_additional))
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(CartPageLocators.delete_button))
        # both do not help with stale element
        time.sleep(3)
        self.browser.find_element(*CartPageLocators.product_additional)
        del_button = self.browser.find_element(*CartPageLocators.delete_button)
        del_button.click()

    def checkout(self):
        button = self.browser.find_element(*CartPageLocators.pay_button)
        button.click()
        assert self.is_element_present(*CartPageLocators.authorization_element), "Authorization method is not presented"

    def remember_price(self):
        overall = self.browser.find_element(*CartPageLocators.overall_price).text
        return overall

    def enter_promo(self):
        input_promo = self.browser.find_element(*CartPageLocators.promo_input)
        input_promo.send_keys('GIVEMEHALYAVA')
        self.browser.find_element(*CartPageLocators.promo_button).click()
        time.sleep(2)
        # added a sleep delay because the server couldn't keep up with the rapid actions being performed

    def check_discount(self, overall):
        price_before = self.turn_text_into_int(overall)
        price_final = self.turn_text_into_int(self.browser.find_element(*CartPageLocators.final_price).text)
        discount = (price_before * 10) // 100
        must_be = price_before - discount
        assert price_final == must_be, f'Expected final price to be with 10% discount {price_before} {price_final}'

    def check_error_message(self):
        assert self.is_element_present(*CartPageLocators.error_message), "Invalid promocode"

    def check_accept_message(self):
        assert self.is_element_present(*CartPageLocators.accept_message), \
              'Excpected to be messege "Coupon code applied successfully"'

    def enter_promo_DC120(self):
        overall_DC120 = self.turn_text_into_int(self.browser.find_element(*CartPageLocators.overall_price).text)
        input_promo = self.browser.find_element(*CartPageLocators.promo_input)
        input_promo.send_keys('DC120')
        self.browser.find_element(*CartPageLocators.promo_button).click()
        self.check_discount_not_applied(overall_DC120)

    def check_discount_not_applied(self, overall_price):
        price_before = overall_price
        price_final = self.turn_text_into_int(self.browser.find_element(*CartPageLocators.final_price).text)
        assert price_final == price_before, 'Expected discount not to be applied due to invalid promocode'

    def enter_promo_with_interception(self):
        for_interception = self.turn_text_into_int(self.browser.find_element(*CartPageLocators.overall_price).text)
        input_promo = self.browser.find_element(*CartPageLocators.promo_input)
        input_promo.send_keys('GIVEMEHALYAVA')
        self.browser.request_interceptor = self.interceptor
        self.browser.find_element(*CartPageLocators.promo_button).click()
        self.check_discount_not_applied(for_interception)

    def interceptor(browser, request):
        if request.url == 'https://pizzeria.skillbox.cc/?wc-ajax=apply_coupon':
            request.abort()

    def check_coupon_not_used_again(self):
        assert not self.is_element_present(*CartPageLocators.promocode_used), "Expected promocode to be not used twice"
