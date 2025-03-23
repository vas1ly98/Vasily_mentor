import time
from playwright.sync_api import Page, expect
from pathlib import Path
from datetime import datetime
# def test_text_box(page: Page):
#     page.goto('https://demoqa.com/text-box')
#
#     # Заполняем поле
#     page.locator('#userName').fill('testQa')
#     page.locator('#userEmail').fill('testQa@mail.ru')
#     page.locator('#currentAddress').fill('улица пушкина')
#     page.locator('#permanentAddress').fill('дом колотушкина')
#     page.click('#submit')
#
#     expect(page.locator('#output #name')).to_have_text('Name:testQa')
#     expect(page.locator('#output #email')).to_have_text('Email:testQa@mail.ru')
#     expect(page.locator('#output #currentAddress')).to_have_text('Current Address :улица пушкина')
#     expect(page.locator('#output #permanentAddress')).to_have_text('Permananet Address :дом колотушкина')

    # time.sleep(5)

def test_box(page: Page):
    page.goto('https://demoqa.com/text-box')
    # page.pause()

    page.fill(selector='[id="userName"]', value='Хозяин')
    page.fill(selector='[id="userEmail"]', value='test@mail.ru')
    page.fill(selector='[id="currentAddress"]', value='улица пушкина')
    page.fill(selector='[id="permanentAddress"]', value='дом колотушкина')
    page.click('#submit')

    expect(page.locator('[id="name"]')).to_have_text('Name:Хозяин')
    expect(page.locator('[id="email"]')).to_have_text('Email:test@mail.ru')
    expect(page.locator('#currentAddress').nth(1)).to_have_text('Current Address :улица пушкина')
    expect(page.locator('#permanentAddress').nth(1)).to_have_text('Permananet Address :дом колотушкина')

    time.sleep(5)