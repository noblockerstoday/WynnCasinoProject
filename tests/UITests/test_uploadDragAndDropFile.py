
from playwright.sync_api import Page, expect


def test_dragAndDropFile(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.locator("#drag-drop-upload").click()
