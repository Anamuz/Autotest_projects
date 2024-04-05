import allure


def test_func(logger):
    logger.debug("Debug message from test_func")
    assert True


@allure.title('Check if search is correct and contains specific word')
def test_search(page):
    with allure.step('Open page https://github.com/microsoft/vscode/issues'):
        page.goto('https://github.com/microsoft/vscode/issues')
        page.set_default_timeout(5000)

        with allure.step('Find search field by ID'):
            el = page.locator('id=js-issues-search')
            el.clear()

        with allure.step('Send "in:title bug"'):
            el.fill('in:title bug')
            el.press('Enter')
            page.wait_for_timeout(5000)

        with allure.step('Find search results'):
            issues = page.query_selector_all('[data-hovercard-type="issue"]')

        with allure.step('Check if search results are correct'):
            for issue in issues:
                title = issue.inner_text()
                assert 'bug' in title.lower(), 'Expected to find "bug" in search results'


@allure.title('Check if search is correct and contains specific author')
def test_author(page):
    page.goto('https://github.com/microsoft/vscode/issues')
    page.set_default_timeout(5000)
    page.click('[title="Author"]')
    page.locator('input#author-filter-field').fill('bpasero')
    page.wait_for_timeout(2000)
    page.locator('button.SelectMenu-item[name="author"]').click()
    search = page.locator('id=js-issues-search')
    value = search.get_attribute('value')
    assert 'bpasero' in value, 'Expected to find "bpasero" in search'


@allure.title('Find out if stars in result >20000')
def test_stars(page):
    page.goto('https://github.com/search/advanced')
    page.set_default_timeout(5000)
    page.locator('id=search_language').select_option('Python')
    page.locator('id=search_stars').fill('>20000')
    page.evaluate("window.scrollBy(0,500)")
    page.locator('id=search_filename').fill('environment.yml')
    page.evaluate("window.scrollBy(0,1000)", "")
    page.locator('div.form-group.flattened button.btn.flex-auto').click()
    page.wait_for_timeout(2000)
    search = page.query_selector_all('a[aria-label*="stars"] span')

    for result in search:
        stars_element = result
        stars_text = stars_element.text_content()
        test_result = True
        quantity = ''

        for number in stars_text:
            if ('0' <= number <= '9'):
                quantity += number
            else:
                quantity += '000'

        star_checknumber = int(quantity)
        if star_checknumber <= 20000:
            assert not test_result, 'Expected to be stars more than 20000 in result'
            break
        else:
            continue
    assert test_result, 'Stars are more than 20000 in search result'


@allure.title('Check if search is correct')
def test_skillbox(page):
    page.goto('https://skillbox.ru/code/', timeout=60000)
    page.set_default_timeout(5000)
    page.set_viewport_size({'width': 1920, 'height': 1080})
    page.evaluate("window.scrollBy(0,700)", "")
    page.wait_for_selector('label[value="profession"]', state='visible')
    page.locator('label[value="profession"] ').click()
    left_slider = page.locator('div[aria-valuetext="1"] .ui-range__dot')
    page.mouse.move(left_slider.bounding_box()['x'], left_slider.bounding_box()['y'])
    page.mouse.down()
    page.mouse.move(left_slider.bounding_box()['x'] + 60, left_slider.bounding_box()['y'])
    page.mouse.up()
    right_slider = page.locator('div[aria-valuetext="24"] .ui-range__dot')
    page.mouse.move(right_slider.bounding_box()['x'], right_slider.bounding_box()['y'])
    page.mouse.down()
    page.mouse.move(right_slider.bounding_box()['x'] - 40, right_slider.bounding_box()['y'])
    page.mouse.up()
    page.evaluate("window.scrollBy(0,400)", "")
    page.click('text=Android')
    page.wait_for_timeout(2000)
    check_profession = page.query_selector_all('.ui-product-card-main__title')
    for element in check_profession:
        assert any(word.lower() in element.text_content().strip().lower() for word in ['android', 'мобильный']), \
              'Expected to be word "Android", "мобильный", "Мобильный" in elements on page'


@allure.title('Check the content of tip')
def test_chart(page):
    page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')
    page.wait_for_selector('.bar.mini', state='visible')
    elements = page.query_selector_all('.bar.mini')
    print(f"Number of elements found: {len(elements)}")

    inside_element = None

    if len(elements) >= 30:
        second_element = elements[20]
        page.mouse.move(second_element.bounding_box()['x'], second_element.bounding_box()['y'])
        inside_element = page.locator('.svg-tip.n').text_content()

    assert inside_element is not None, 'No elements found that satisfy the condition'

    assert inside_element == '251 commits the week of May 21', \
        f'Expected to be "251 commits the week of May 21" in {inside_element}'
