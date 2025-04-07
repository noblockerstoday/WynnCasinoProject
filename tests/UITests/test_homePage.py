from playwright.sync_api import Page, expect


def test_homePage(page:Page):
    # navigating to Landing Page
    page.goto("https://the-internet.herokuapp.com/upload")

    # assertion to verify text is as expected
    expect(page.get_by_text("File Uploader")).to_be_visible()
    expect(page.get_by_text("Choose a file on your system and then click upload. Or, drag and drop a file into the area below.")).to_be_visible()
