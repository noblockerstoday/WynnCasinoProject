from playwright.sync_api import Page, expect


def test_homePageFooterLink(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    with (page.expect_popup() as newPage):
        page.locator(".large-4").click()
        childPage = newPage.value
        text = childPage.locator(".hero__title").text_content()
        expect(childPage.locator(".hero__title")).to_contain_text("Elemental Selenium")
        #print(text)


