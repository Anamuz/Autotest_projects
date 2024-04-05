from src.pages.main_page import MainPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.registration_page import RegisterPage
from src.exceptions.custom_exceptions import CheckoutError
import allure


@allure.title('First scenario: Use of correct promocode')
def test_promo_gives_discount(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Add products'):
        page.add_products()
    with allure.step('Go to cart page'):
        page = CartPage(browser, link)
        page.go_to_cart()
    with allure.step('Use promocode GIVEMEHALYAVA'):
        overall = page.remember_price()
        page.enter_promo()
        page.check_accept_message()
        page.check_discount(overall)


@allure.title('Second scenario: Use of Invalid promocode')
def test_discount_absence_with_invalid_promocode(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Add products'):
        page.add_products()
    with allure.step('Go to cart page'):
        page = CartPage(browser, link)
        page.go_to_cart()
    with allure.step('Use promocode DC120'):
        page.remember_price()
        page.enter_promo_DC120()
        page.check_error_message()


@allure.title('Third scenario: Request interception')
def test_discount_absence_with_blocked_request(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Add products'):
        page.add_products()
    with allure.step('Go to cart page'):
        page = CartPage(browser, link)
        page.go_to_cart()
    with allure.step('Intercept request'):
        page.remember_price()
        page.enter_promo_with_interception()


@allure.title('Fourth scenario: Promocode reuse')
def test_promocode_reuse(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Register new user'):
        page = RegisterPage(browser, link)
        page.register()
        page.return_to_main_page()
    with allure.step('Add products'):
        page.add_products()
    with allure.step('Go to cart page'):
        page = CartPage(browser, link)
        page.go_to_cart()
    with allure.step('Use promo'):
        page.enter_promo()
    with allure.step('Complete checkout'):
        page = CheckoutPage(browser, link)
        page.go_to_checkout()
        page.complete_checkout()
        page.draw_up_checkout()
    with allure.step('Create another order'):
        page.return_to_main_page()
        page.add_products()
        page = CartPage(browser, link)
        page.go_to_cart()
    with allure.step('Use promo again'):
        page.enter_promo()
        page.check_coupon_not_used_again()
    with allure.step('Complete new checkout with promo again'):
        page = CheckoutPage(browser, link)
        page.go_to_checkout()
        page.complete_checkout()
        try:
            page.draw_up_checkout()
        except CheckoutError:
            allure.attach("Error", "Checkout completed with promo code used again")
            assert False, "Expected error due to promo code being used again"
