import time
from pathlib import Path
from playwright.sync_api import Page, expect


def test_chooseFileButton(page:Page):
    # setting the fle path of the .txt file
    file_path = Path(__file__).parent / "TestData.txt"

    # navigating to Landing Page
    page.goto("https://the-internet.herokuapp.com/upload")

    # select and upload .txt file
    # unable to target this page element and upload .txt file
    # click event works but navigates user to their OS file loader
    # instead, we want to target .txt file and write an assertion upon successful upload
    ############### TO CONTINUE WORKING
    page.set_input_files("input#drag-drop-upload", str("TestData.txt"))

    # assertion to verify the .txt file has been successfully uploaded
    #expect(page.locator(".example")).to_contain_text("File Uploaded!")




