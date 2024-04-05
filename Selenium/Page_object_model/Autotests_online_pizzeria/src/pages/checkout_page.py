from .base_page import BasePage
from .locators import CheckoutPageLocators
from .locators import CartPageLocators
from datetime import date
import datetime
from selenium.common.exceptions import UnexpectedAlertPresentException


class CheckoutPage(BasePage):
    def go_to_checkout(self):
        button = self.browser.find_element(*CartPageLocators.pay_button)
        button.click()

    def complete_checkout(self):
        form_name = self.browser.find_element(*CheckoutPageLocators.name)
        form_name.send_keys('User_Name')
        form_surname = self.browser.find_element(*CheckoutPageLocators.surname)
        form_surname.send_keys('User_Surname')
        self.browser.find_element(*CheckoutPageLocators.country_dropdown).click()
        country = self.browser.find_element(*CheckoutPageLocators.country)
        country.click()
        form_address = self.browser.find_element(*CheckoutPageLocators.address)
        form_address.send_keys('User_Address')
        form_city = self.browser.find_element(*CheckoutPageLocators.city)
        form_city.send_keys('User_City')
        form_state = self.browser.find_element(*CheckoutPageLocators.state)
        form_state.send_keys('User_State')
        form_postcode = self.browser.find_element(*CheckoutPageLocators.postcode)
        form_postcode.send_keys('123456')
        form_phone = self.browser.find_element(*CheckoutPageLocators.phone)
        form_phone.send_keys('+79876543221')
        form_date = self.browser.find_element(*CheckoutPageLocators.calendar)
        formatted_date = self.format_date()
        form_date.send_keys(formatted_date)
        form_comment = self.browser.find_element(*CheckoutPageLocators.comment)
        form_comment.send_keys('User_Comment')
        form_terms = self.browser.find_element(*CheckoutPageLocators.terms)
        form_terms.click()
        return formatted_date

    def choose_payment(self):
        self.browser.find_element(*CheckoutPageLocators.payment_method).click()

    def draw_up_checkout(self):
        self.browser.find_element(*CheckoutPageLocators.order_button).click()

    def format_date(self):
        today = date.today()
        tomorrow = today + datetime.timedelta(days=1)
        date_str = tomorrow.strftime('%d%m%Y')
        return date_str

    def check_info(self, formatted_date, email):
        name = 'User_Name'
        surname = 'User_Surname'
        address = 'User_Address'
        city = 'User_City'
        state = 'User_State'
        postcode = '123456'
        detailes = [name, surname, address, city, state, postcode]
        phone = '+79876543221'
        payment_method = 'Оплата при доставке'
        note = 'User_Comment'
        date = f"{formatted_date[0:2]}.{formatted_date[2:4]}.{formatted_date[4:]}"
        mail = email
        user_details_elements = self.browser.find_elements(*CheckoutPageLocators.overview_user_details)
        user_details_text = ''.join([element.text for element in user_details_elements])
        entered_phone = self.browser.find_element(*CheckoutPageLocators.overview_phone).text
        entered_payment_method = self.browser.find_element(*CheckoutPageLocators.overview_payment_method).text
        entered_note = self.browser.find_element(*CheckoutPageLocators.overview_comment).text
        entered_date = self.browser.find_element(*CheckoutPageLocators.overview_date).text
        entered_email = self.browser.find_element(*CheckoutPageLocators.overview_email).text
        assert all(detail in user_details_text for detail in detailes), \
            f"Expected to be {detailes} in {user_details_text}"
        assert phone in entered_phone, \
            f"Expected to be {phone} in {entered_phone}"
        assert payment_method in entered_payment_method, \
            f"Expected to be {payment_method} in {entered_payment_method}"
        assert note in entered_note, \
            f"Expected to be {note} in {entered_note}"
        assert mail in entered_email, \
            f"Expected to be {mail} in {entered_email}"
        assert date in entered_date, \
            f"Expected to be {date} in {entered_date}"

    def price_check(self, price):
        to_compare = price
        total = self.browser.find_element(*CheckoutPageLocators.total_price).text
        assert total in to_compare, \
            f"Expected to be {total} = {to_compare}"

    def return_to_main_page(self):
        self.browser.find_element(*CheckoutPageLocators.return_to_main).click()
        try:
            self.browser.switch_to.alert.accept()
        except UnexpectedAlertPresentException:
            self.browser.switch_to.alert.accept()
