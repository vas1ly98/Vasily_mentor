import time
from playwright.sync_api import Page, expect
from random import randint

def test_text_box(page: Page):
    page.goto('https://dev-cinescope.coconutqa.ru/register')

    page.fill(selector='[data-qa-id="register_full_name_input"]', value='Хозяин Этого Сайта')

    page.fill(selector='[data-qa-id="register_email_input"]', value=f'test_{randint(1, 9999)}@email.qa')

    page.fill(selector='[data-qa-id="register_password_input"]', value='Qfafafaf213')

    page.fill(selector='[data-qa-id="register_password_repeat_input"]', value='Qfafafaf213')

    page.click('[data-qa-id="register_submit_button"]')

    page.wait_for_url('https://dev-cinescope.coconutqa.ru/login')
    expect(page.get_by_text("Подтвердите свою почту")).to_be_visible(visible=True)

    time.sleep(10)
