import time
from pathlib import Path

from playwright.sync_api import Page, expect

def test_chooseFileButton(page:Page):
    # setting the fle path of the .txt file
    file_path = Path(__file__).parent / "TestData.txt"

    # navigating to Landing Page
    page.goto("https://the-internet.herokuapp.com/upload")

    # select and upload .txt file
    page.set_input_files("input#file-upload",str("TestData.txt"))
    page.get_by_role("button", name="Upload").click()

    # assertion to verify the .txt file has been successfully uploaded
    expect(page.locator(".example")).to_contain_text("File Uploaded!")
