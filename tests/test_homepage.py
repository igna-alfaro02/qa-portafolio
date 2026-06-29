from playwright.sync_api import sync_playwright

def test_homepage_title():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.wait_for_timeout(3000) 

        page.goto("https://www.saucedemo.com")

        page.wait_for_timeout(3000) 

        assert "Swag Labs" in page.title()

        page.wait_for_timeout(3000) 

        browser.close()