from playwright.sync_api import sync_playwright
import time

from pytest_playwright.pytest_playwright import browser, context
from sqlalchemy import false


def test_some_entities():
    with sync_playwright() as p:
        browser1 = p.chromium.launch(headless=False)

        context1_1 = browser1.new_context()
        context1_2 = browser1.new_context()

        page1_1_1 = context1_1.new_page()
        page1_1_2 = context1_1.new_page()
        page1_2_1 = context1_2.new_page()
        page1_2_2 = context1_2.new_page()

        page1_1_1.goto("https://vk.com/audios135442746?q=%D0%9A%D0%BE%D1%81%D0%BC%D0%BE%D1%81%20(feat.%20DEAD%20BLONDE)%20Slava%20KPSS&section=all")
        page1_1_2.goto("https://thankful-candy-c57.notion.site/1af94f774aab80108ee7fa72fa52b328?pvs=25")
        page1_2_1.goto("https://www.shazam.com/song/1649487615/%D0%BA%D0%BE%D1%81%D0%BC%D0%BE%D1%81-feat-dead-blonde")
        page1_2_2.goto("https://www.yandex.ru")

        time.sleep(7)

        # Закрываем пейджи
        page1_1_1.close()
        page1_1_2.close()
        page1_2_1.close()
        page1_2_2.close()

        # Закрываем контексты
        context1_1.close()
        context1_2.close()

        # Закрываем браузер
        browser1.close()
