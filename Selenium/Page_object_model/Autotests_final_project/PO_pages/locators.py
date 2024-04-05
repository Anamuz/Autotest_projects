from selenium.webdriver.common.by import By


class BasePageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")
    user_icon = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_form = (By.ID, "login_form")
    register_form = (By.ID, "register_form")


class ProductPageLocators:
    add_to_cart_btn = (By.CSS_SELECTOR, ".btn-add-to-basket")
    succesfull_text = (By.XPATH, '(//div[@class="alertinner "])[1]')
    product_name_is = (By.CSS_SELECTOR, '.product_main h1')
    add_product_name = (By.CSS_SELECTOR, "#messages div.alertinner > strong")
    product_price_is = (By.CSS_SELECTOR, 'div.product_main > p.price_color')
    price_in_cart = (By.CSS_SELECTOR, "#messages div.alertinner > p > strong")
    succes_message = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    go_to_cart_btn = (By.CSS_SELECTOR, "div.basket-mini span a.btn.btn-default")
    products = (By.CSS_SELECTOR, ".basket-items")
    text_empty = (By.CSS_SELECTOR, "#content_inner p")


class RegistrationLocators:
    e_mail = (By.NAME, 'registration-email')
    password_1 = (By.NAME, 'registration-password1')
    password_2 = (By.NAME, 'registration-password2')
    reg_button = (By.NAME, 'registration_submit')
