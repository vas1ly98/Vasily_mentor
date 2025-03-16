from playwright.sync_api import sync_playwright
import time

def test_text_box():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # <- Открываем браузер
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://demoqa.com/text-box')
        page.locator('#userName').fill('testQa')

        assert page.locator('#userName').input_value() == 'testQa'
        time.sleep(10)

        page.close()
        browser.close()