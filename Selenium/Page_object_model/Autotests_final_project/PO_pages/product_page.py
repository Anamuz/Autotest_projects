from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_promo_url(self, browser):
        assert "?promo=newYear" in browser.current_url, 'Excpected promo in link'

    def add_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.add_to_cart_btn)
        button.click()

    translations = {
        'ru': 'был добавлен в вашу корзину',
        'en': 'has been added to your basket',
        'fr': 'a été ajouté à votre panier',
        'ca': "s'ha afegit a la seva cistella",
        'cs': 'byla přidána do vašeho košíku',
        'da': 'er lagt i din indkøbskurv',
        'de': 'wurde Ihrem Warenkorb hinzugefügt',
        'es': 'ha sido añadido al carrito',
        'fi': 'lisätty koriisi',
        'it': 'è stato aggiunto al tuo carrello',
        'ko': '이(가) 장바구니에 추가되었습니다',
        'nl': 'is toegevoegd aan je winkelmand',
        'pl': 'został dodany do koszyka',
        'pt': 'foi adicionado ao seu carrinho',
        'pt-br': 'foi adicionado à sua cesta',
        'ro': 'a fost adaugat in cos',
        'sk': 'bol pridaný do košíka',
        'uk': 'було додано до Вашого кошику'
        }

    def check_add_to_cart(self, user_language):
        text_check_add = self.translations.get(user_language, self.translations['en'])
        text_about_add = self.browser.find_element(*ProductPageLocators.succesfull_text).text
        assert text_check_add in text_about_add, f'Expected text: {text_check_add}, but got {text_about_add}'

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.product_name_is).text
        added_product = self.browser.find_element(*ProductPageLocators.add_product_name).text
        print(product_name)
        print(added_product)
        assert product_name == added_product, 'Expected that product name and its name in cart are similar'

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.product_price_is).text
        compare_price = self.browser.find_element(*ProductPageLocators.price_in_cart).text
        assert price == compare_price, 'Expected that price of product and in cart are similar'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.succes_message), \
            "Success message is presented, but should not be"

    def should_not_appear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.succes_message), \
            "Success message is presented, but should not be"
