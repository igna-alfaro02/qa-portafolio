from playwright.sync_api import sync_playwright

def test_login_saucedemo():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.wait_for_timeout(3000) 

        page.fill('[data-test="username"]', 'standard_user')

        page.wait_for_timeout(3000) 

        page.fill('[data-test="password"]', 'secret_sauce')

        page.wait_for_timeout(3000) 

        page.click('[data-test="login-button"]')

        page.screenshot(path="screenshots/login_success.png")

        page.wait_for_timeout(3000) 

        assert "inventory" in page.url

        browser.close() 

        