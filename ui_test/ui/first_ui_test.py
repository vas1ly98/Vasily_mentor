import time
from playwright.sync_api import Page, expect
from ui_test.utils.conftest import page

def test_text_box(page: Page):
    page.goto('https://demoqa.com/text-box')

    # Заполняем поле
    page.locator('#userName').fill('testQa')
    page.locator('#userEmail').fill('testQa@mail.ru')
    page.locator('#currentAddress').fill('улица пушкина')
    page.locator('#permanentAddress').fill('дом колотушкина')
    page.click('#sumbit')

    expect(page.locator('#output #name')).to_have_text('Name:testQa')
    expect(page.locator('#output #email')).to_have_text('Email:testQa@mail.ru')
    expect(page.locator('#output #currentAddress')).to_have_text('Current Address :улица пушкина')
    expect(page.locator('#output #permanentAddress')).to_have_text('Permananet Address :дом колотушкина')

    time.sleep(5)