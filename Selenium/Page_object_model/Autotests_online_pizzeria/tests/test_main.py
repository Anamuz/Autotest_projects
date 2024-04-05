from src.pages.main_page import MainPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.menu_page import MenuPage
from src.pages.product_page import ProductPage
from src.pages.registration_page import RegisterPage
from src.pages.login_page import LoginPage
import allure


@allure.title('Main flow')
def test_user_flow(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
        page.should_be_slider()
        with allure.step('Choose first pizza'):
            first_pizza = page.choose_pizza()
            page.should_be_cart_button()
        with allure.step('Check work of slider'):
            page.run_through_right()
            page.run_through_left()
        with allure.step('Add another pizza'):
            second_pizza = page.add_second_pizza()
        with allure.step('Go to product page'):
            page.open_pizza_page()
        page_product = ProductPage(browser, link)
        with allure.step("Add pizzas' side"):
            page_product.should_be_additional_options()
            third_pizza = page_product.add_additional_options()
    page_cart = CartPage(browser, link)
    with allure.step('Go to cart page'):
        page_cart.go_to_cart()
        with allure.step('Work with products in cart'):
            page_cart.check_products(first_pizza, second_pizza, third_pizza)
            with allure.step('Change quantity of products'):
                page_cart.change_quantity()
            with allure.step('Delete product'):
                page_cart.delete_product()
    page_menu = MenuPage(browser, link)
    with allure.step('Go to Menu Page'):
        page_menu.go_to_dessert()
        with allure.step('Choose dessert'):
            page_menu.price_filter()
            page_menu.choose_dessert()
    page_cart = CartPage(browser, link)
    with allure.step('Go to checkout page'):
        page_cart.go_to_cart()
        page_cart.checkout()
    page_register = RegisterPage(browser, link)
    with allure.step('Registrate new user'):
        page_register.register()
    page_login = LoginPage(browser, link)
    with allure.step('Check if logged'):
        email = page_login.should_be_logged()
    page_cart = CartPage(browser, link)
    with allure.step('Back to checkout page'):
        page_cart.go_to_cart()
        price = page_cart.remember_price()
        page_checkout = CheckoutPage(browser, link)
        page_checkout.go_to_checkout()
        with allure.step('Complete checkout'):
            date = page_checkout.complete_checkout()
            page_checkout.choose_payment()
            page_checkout.draw_up_checkout()
            page_checkout.price_check(price)
            page_checkout.check_info(date, email)
