from src.pages.main_page import MainPage
from src.pages.bonus_page import BonusPage
import allure


@allure.title('Scenario: Register bonus program')
def test_bonus_program_registration(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Go to bonus program page'):
        page = BonusPage(browser, link)
        page.go_bonus_page()
        page.should_be_bonus_page()
    with allure.step('Enter details'):
        page.enter_details()
        page.alert_message()
    with allure.step('The card is issued'):
        page.card_issued_message()


@allure.title('Check validation in forms')
def test_bonus_program_input_validation(browser):
    link = "https://pizzeria.skillbox.cc/"
    page = MainPage(browser, link)
    with allure.step('Open page https://pizzeria.skillbox.cc/'):
        page.open()
    with allure.step('Go to bonus program page'):
        page = BonusPage(browser, link)
        page.go_bonus_page()
        page.should_be_bonus_page()
    with allure.step('Check validation'):
        page.enter_invalid_details()
