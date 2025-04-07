import time

from playwright.sync_api import Page, expect


def test_homePageFooterLink(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.get_by_role("img", name="Fork me on GitHub").click()

    # assertion to verify end user is navigated to GitHub repos after click event
    (expect(page).to_have_url('https://github.com/saucelabs/the-internet'))
    time.sleep(4)
