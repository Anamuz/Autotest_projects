from selenium.webdriver.common.by import By


class BasePageLocators:
    slider = (By.CSS_SELECTOR, ".product-slider")
    cart_button = (By.CSS_SELECTOR, ".item-img a.add_to_cart_button")
    left_slider_button = (By.CSS_SELECTOR, '.slick-prev')
    right_slider_button = (By.CSS_SELECTOR, '.slick-next')
    first_pizza_name = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(4) .item-img ~ a h3")
    first_product = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(4) .item-img")
    first_product_button = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(4) .item-img a.add_to_cart_button")
    another_pizza_name = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(6) .item-img ~ a h3")
    another_pizza_button = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(6) .item-img a.add_to_cart_button")
    third_pizza_name = (By.CSS_SELECTOR, ".prod1-slider li:nth-child(5) .item-img ~ a h3")
    second_product = (By.CSS_SELECTOR, ".prod2-slider li:nth-child(1) .item-img")
    second_product_button = (By.CSS_SELECTOR, ".prod2-slider li:nth-child(1) .item-img a.add_to_cart_button")


class BonusPageLocators():
    bonus_page = (By.CSS_SELECTOR, "#menu-item-363")
    name = (By.CSS_SELECTOR, '#bonus_username')
    phone = (By.CSS_SELECTOR, '#bonus_phone')
    order_card = (By.CSS_SELECTOR, 'button[name="bonus"]')
    success_text = (By.CSS_SELECTOR, '#bonus_main h3')
    validation_message = (By.CSS_SELECTOR, 'p ~ #bonus_content')


class LoginPageLocators:
    to_myacc = (By.CSS_SELECTOR, "#menu-item-30")
    edit = (By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--edit-account a")
    email = (By.CSS_SELECTOR, "#account_email")
    myacc_content = (By.CSS_SELECTOR, ".woocommerce-MyAccount-content")


class ProductPageLocators:
    pizza_title = (By.CSS_SELECTOR, ".product_title")
    additional = (By.CSS_SELECTOR, ".cart .select")
    option = (By.CSS_SELECTOR, "#board_pack option:nth-child(2)")
    cart = (By.CSS_SELECTOR, ".single_add_to_cart_button")


class CheckoutPageLocators:
    name = (By.CSS_SELECTOR, "#billing_first_name")
    surname = (By.CSS_SELECTOR, "#billing_last_name")
    country_dropdown = (By.CSS_SELECTOR, "#select2-billing_country-container")
    country = (By.CSS_SELECTOR, ".select2-results__option:nth-child(182)")
    address = (By.CSS_SELECTOR, "#billing_address_1")
    city = (By.CSS_SELECTOR, "#billing_city")
    state = (By.CSS_SELECTOR, "#billing_state")
    postcode = (By.CSS_SELECTOR, "input#billing_postcode")
    phone = (By.CSS_SELECTOR, "#billing_phone")
    calendar = (By.CSS_SELECTOR, "#order_date")
    comment = (By.CSS_SELECTOR, "#order_comments")
    payment_method = (By.CSS_SELECTOR, ".payment_method_cod label")
    terms = (By.CSS_SELECTOR, ".woocommerce-terms-and-conditions-checkbox-text")
    order_button = (By.CSS_SELECTOR, "#place_order")
    overview_date = (By.CSS_SELECTOR, ".woocommerce-order-overview__date strong")
    overview_email = (By.CSS_SELECTOR, ".woocommerce-order-overview__email strong")
    overview_payment_method = (By.CSS_SELECTOR, ".woocommerce-order-overview__payment-method strong")
    overview_comment = (By.CSS_SELECTOR, "table.order_details tfoot tr:last-child td")
    overview_user_details = (By.CSS_SELECTOR, ".woocommerce-customer-details address")
    overview_phone = (By.CSS_SELECTOR, ".woocommerce-customer-details--phone")
    total_price = (By.CSS_SELECTOR, "tfoot tr:nth-child(3) .woocommerce-Price-amount")
    return_to_main = (By.CSS_SELECTOR, "#menu-item-26")


class CartPageLocators:
    cart_button = (By.CSS_SELECTOR, ".cart-contents")
    change_quantity = (By.CSS_SELECTOR, ".quantity input")
    delete_button = (By.CSS_SELECTOR, ".product-remove .remove")
    promo_input = (By.CSS_SELECTOR, ".coupon .input-text")
    promo_button = (By.CSS_SELECTOR, ".coupon .button")
    error_message = (By.CSS_SELECTOR, ".woocommerce-notices-wrapper .woocommerce-error")
    accept_message = (By.CSS_SELECTOR, ".woocommerce-notices-wrapper .woocommerce-message")
    update_button = (By.CSS_SELECTOR, 'button[name="update_cart"]')
    pay_button = (By.CSS_SELECTOR, ".checkout-button")
    product_title = (By.CSS_SELECTOR, ".product-name a")
    product_additional = (By.CSS_SELECTOR, ".product-name dl p")
    overall_price = (By.CSS_SELECTOR, ".cart-subtotal .amount bdi")
    final_price = (By.CSS_SELECTOR, ".order-total .amount bdi")
    coupon_name = (By.CSS_SELECTOR, ".cart-discount th")
    authorization_element = (By.CSS_SELECTOR, '.showlogin')
    promocode_used = (By.CSS_SELECTOR, ".cart-discount")


class MenuPageLocators:
    menu = (By.CSS_SELECTOR, "#menu-item-389 a")
    menu_desserts = (By.CSS_SELECTOR, ".menu-item:nth-child(2) .sub-menu #menu-item-391")
    right_slider = (By.CSS_SELECTOR, ".price_slider .ui-slider-handle:nth-child(3)")
    filter_button = (By.CSS_SELECTOR, ".price_slider_amount .button")
    dessert_price = (By.CSS_SELECTOR, ".product_cat-deserts .amount bdi")
    dessert_button = (By.CSS_SELECTOR, ".price-cart .button")


class RegistrationPageLocators:
    my_acc = (By.CSS_SELECTOR, "#menu-item-30 a")
    go_to_registration = (By.CSS_SELECTOR, ".custom-register-button")
    username = (By.CSS_SELECTOR, '[name="username"]')
    email = (By.CSS_SELECTOR, '[name="email"]')
    password = (By.CSS_SELECTOR, '[name="password"]')
    register_button = (By.CSS_SELECTOR, '[name="register"]')
    return_to_main = (By.CSS_SELECTOR, "#menu-item-26")
