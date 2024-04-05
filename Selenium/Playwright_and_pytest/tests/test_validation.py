from selenium import webdriver
import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def test_func(logger):
    logger.debug("Debug message from test_func")
    assert True


@allure.title('Check if search is correct and contains specific word')
def test_search(driver_setup: WebDriver):
    driver = driver_setup
    with allure.step('Open page https://github.com/microsoft/vscode/issues'):
        driver.get('https://github.com/microsoft/vscode/issues')
    action_chains = webdriver.ActionChains(driver)
    with allure.step('Find search field by ID'):
        el = driver.find_element(By.ID, 'js-issues-search')
    with allure.step('Clear field'):
        el.clear()
    with allure.step('Send "in:title bug"'):
        el.send_keys('in:title bug')
    action_chains.send_keys(Keys.ENTER).perform()
    driver.implicitly_wait(5)
    with allure.step('Find search results'):
        issues = driver.find_elements(By.XPATH, "//div[contains(@class, 'js-issue-row')]")
    with allure.step('Check if search results are correct'):
        for issue in issues:
            title = issue.find_element(By.XPATH, ".//a[contains(@class, 'Link--primary v-align-middle')]").text
            assert 'bug' in title.lower(), 'Expected to find "bug" in search results'


@allure.title('Check if search is correct and contains specific author')
def test_author(driver_setup: WebDriver):
    driver = driver_setup
    driver.get('https://github.com/microsoft/vscode/issues')
    driver.find_element(By.XPATH, '//*[contains(text(), "Author")]').click()
    driver.implicitly_wait(5)
    el = driver.find_element(By.ID, 'author-filter-field')
    el.send_keys('bpasero')
    driver.find_element(By.XPATH, "//*[contains(@class, 'SelectMenu-item d-block js-new-item-value')]")
    search = driver.find_element(By.ID, 'js-issues-search')
    assert search.get_attribute('value') == 'bpasero', 'Expected to find "bpasero" in search'


@allure.title('Find out if stars in result >20000')
def test_stars(driver_setup: WebDriver):
    driver = driver_setup
    driver.get('https://github.com/search/advanced')
    driver.find_element(By.ID, 'search_language').click()
    driver.find_element(By.XPATH, '//*[@id="search_language"]/optgroup[1]/option[19]').click()
    search_input = driver.find_element(By.ID, 'search_stars')
    search_input.send_keys('>20000')
    driver.execute_script("window.scrollBy(0,500)", "")
    search_filename = driver.find_element(By.ID, 'search_filename')
    search_filename.send_keys('environment.yml')
    driver.execute_script("window.scrollBy(0,1000)", "")
    driver.find_element(By. XPATH, '//*[@class="btn flex-auto"]').click()
    driver.implicitly_wait(3)
    search = driver.find_elements(By.CSS_SELECTOR, 'a[aria-label*="stars"]')

    for result in search:
        stars = result.text
        test_result = True
        quantity = ''

        for number in stars:
            if ('0' <= number <= '9'):
                quantity += number
            else:
                quantity += '000'

        star_checknumber = int(quantity)
        if star_checknumber <= 20000:
            # assert test_result == False
            assert not test_result, 'Expected to be stars more than 20000 in result'
            break
        else:
            continue
    assert test_result, 'Stars are more than 20000 in search result'


@allure.title('Check if search is correct')
def test_skillbox(driver_setup: WebDriver):
    driver = driver_setup
    driver.get('https://skillbox.ru/code/')
    action_chains = webdriver.ActionChains(driver)
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0,700)", "")
    driver.find_element(By.XPATH,
                        '//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[2]/ul/li[2]/label/span').click()
    left_slider = driver.find_element(By.CSS_SELECTOR, 'div[aria-valuetext="1"] .ui-range__dot')
    action_chains\
        .click_and_hold(left_slider)\
        .move_by_offset(60, 0)\
        .release()\
        .perform()
    right_slider = driver.find_element(By.CSS_SELECTOR, 'div[aria-valuetext="24"] .ui-range__dot')
    action_chains\
        .click_and_hold(right_slider)\
        .move_by_offset(-40, 0)\
        .release()\
        .perform()
    driver.execute_script("window.scrollBy(0,400)", "")
    driver.find_element(By.XPATH, '//span[contains(@class, "filter-checkboxes-list__value")]\
                        [contains(text(), "Android")]').click()
    driver.implicitly_wait(5)
    check_profession = driver.find_elements(By.CSS_SELECTOR, '.ui-product-card-main__title')
    for element in check_profession:
        assert any(word in element.text for word in ['Android', 'мобильный', 'Мобильный']), \
              'Expected to be word "Android", "мобильный", "Мобильный" in elements on page'


@allure.title('Check the content of tip')
def test_chart(driver_setup):
    driver = driver_setup
    driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
    driver.implicitly_wait(10)
    action_chains = webdriver.ActionChains(driver)
    element = driver.find_elements(By.CSS_SELECTOR, '.bar')
    if len(element) >= 30:
        second_element = element[20]
        action_chains.move_to_element(second_element).perform()
        inside_element = driver.find_element(By.CSS_SELECTOR, '.svg-tip.n')
    assert inside_element.text == '251 commits the week of May 21', \
        f'Expected to be "251 commits the week of May 21" in {inside_element.text}'
