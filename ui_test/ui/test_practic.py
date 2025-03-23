import time
from playwright.sync_api import Page, expect
from pathlib import Path
from datetime import datetime

# def test_box(page: Page):
#     page.goto('https://demoqa.com/webtables')
#
#     page.get_by_role('button', name='Add').click()
#     expect(page.get_by_text("Registration Form")).to_be_visible(visible=True)
#     page.fill(selector='[id="firstName"]', value='жора')
#     page.fill(selector='[id="lastName"]', value='петров')
#     page.fill(selector='[id="userEmail"]', value='jora@mail.ru')
#     page.fill(selector='[id="age"]', value='18')
#     page.get_by_role("textbox", name='Salary').fill('1000')
#     page.get_by_role('textbox', name='Department').fill('USA')
#     time.sleep(5)
#     page.get_by_role('button', name='Submit').click()
#
#     time.sleep(5)

# def test_box_two(page: Page):
#     current_date = datetime.today().strftime('%d %b %Y')
#     page.goto('https://demoqa.com/automation-practice-form')
#     page.fill(selector='[id="firstName"]', value='хозяин')
#     page.fill(selector='[id="lastName"]', value='Иванов')
#     page.get_by_role('textbox', name='name@example.com').fill('jora@mail.ru')
#     page.check('input#gender-radio-2', force=True)
#     page.get_by_role('textbox', name='Mobile Number').fill('8902929291')
#
#     value = page.get_attribute('#dateOfBirthInput', 'value')
#     assert value == current_date
#
#     page.locator('.subjects-auto-complete__input input').fill('Math')
#     page.locator('label[for="hobbies-checkbox-2"]').click(force=True)
#     page.fill('#currentAddress', 'улица пушкина')
#
#     page.locator('#state').click()
#     # Клик по опции "Uttar Pradesh"
#     page.locator('div[id="react-select-3-option-0"]').click()
#     time.sleep(2)
#
#     page.locator('#city svg').click()
#     time.sleep(2)
#     page.locator('div#react-select-4-option-0').click()
#
#     # Находим элемент <span> в футере
#     footer_span_locator = page.locator('footer span')
#
#     # Получаем текст содержимого
#     message = footer_span_locator.text_content()
#
#     # Проверяем, что текст совпадает
#     assert message == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#     page.get_by_role('button', name='Submit').click()
#     time.sleep(5)


# def test_home_work_two(page: Page):
#     page.goto('https://demoqa.com/checkbox')
#     page.wait_for_load_state('domcontentloaded')
#
#     # Проверяем, что Home видим (используем текстовый селектор для "Home")
#     assert page.is_visible('span.rct-title >> text=Home') == True
#
#     # Проверяем, что Desktop не виден
#     assert page.is_visible('span.rct-title >> text=Desktop') == False
#
#     # Кликаем по кнопке Toggle для раскрытия списка
#     page.get_by_role('button', name='Toggle').click()
#
#     # Проверяем, что Desktop стал видимым
#     assert page.is_visible('span.rct-title >> text=Desktop') == True



def test_home_work_free(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    assert not page.is_visible(selector='[id="visibleAfter"]')
    page.wait_for_selector(selector='[id="visibleAfter"]', state='visible', timeout=10000)
    assert page.is_visible('#visibleAfter')


def test_home_work_one(page: Page):
    page.goto('https://demoqa.com/radio-button')
    page.wait_for_load_state('domcontentloaded')


    assert page.is_enabled('#yesRadio') == True
    assert page.is_enabled('#impressiveRadio') == True
    assert page.is_enabled('#noRadio') == False

def test_expect(page: Page):
    page.goto("https://demoqa.com/radio-button")
    yes_radio = page.get_by_role("radio", name="Yes")
    impressive_radio = page.get_by_role("radio", name="Impressive")
    no_radio = page.get_by_role("radio", name="No")
    expect(no_radio).to_be_disabled()  # проверяем, что не доступен
    expect(yes_radio).to_be_enabled()  # проверяем, что доступен
    expect(impressive_radio).to_be_enabled()  # проверяем, что доступен
    page.locator('[for="yesRadio"]').click()  # тут хитрый лейбл не позволяет кликнуть прямо на инпут, обращаемся по лейблу
    expect(yes_radio).to_be_checked()  # проверяем, что отмечен
    expect(impressive_radio).not_to_be_checked()  # проверяем, что не отмечен
