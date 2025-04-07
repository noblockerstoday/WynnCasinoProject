from playwright.sync_api import Page, expect


def test_uploadError(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    page.get_by_role("button", name="Upload").click()

    # assertion to verify end user is presented with an Internal Server Error
    # when no file is uploaded
    expect(page.locator("body")).to_contain_text("Internal Server Error")
