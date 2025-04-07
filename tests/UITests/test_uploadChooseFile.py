import time

from playwright.sync_api import Page, expect


def test_chooseFileButton(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#file-upload").click()
    time.sleep(5)
