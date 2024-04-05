from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def to_cart(self):
        button = self.browser.find_element(*BasketPageLocators.go_to_cart_btn)
        button.click()

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.products), \
            "Products are presented, but should not be"

    translations = {
        'ru': 'Ваша корзина пуста',
        'en': 'Your basket is empty',
        'fr': 'Votre panier est vide',
        'ar': 'سلة التسوق فارغة',
        'ca': 'La seva cistella està buida',
        'cs': 'Váš košík je prázdný',
        'da': 'Din indkøbskurv er tom',
        'de': 'Ihr Warenkorb ist leer',
        'el': 'Το καλάθι σας είναι άδειο',
        'es': 'Tu carrito esta vacío',
        'fi': 'Korisi on tyhjä',
        'it': 'Il tuo carrello è vuoto',
        'ko': '장바구니가 비었습니다',
        'nl': 'Je winkelmand is leeg',
        'pl': 'Twój koszyk jest pusty',
        'pt': 'O carrinho está vazio',
        'pt-br': 'Sua cesta está vazia',
        'ro': 'Cosul tau este gol',
        'sk': 'Váš košík je prázdny',
        'uk': 'Ваш кошик пустий'
    }

    def should_be_text_empty_cart(self, user_language):
        text_check = self.translations.get(user_language, self.translations['en'])
        result_text = self.browser.find_element(*BasketPageLocators.text_empty).text
        assert text_check in result_text, f'Expected text: {text_check}, but got {result_text}'
