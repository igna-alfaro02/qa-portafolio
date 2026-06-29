from playwright.sync_api import sync_playwright

def test_invalid_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://www.saucedemo.com")

        page.wait_for_timeout(3000) 

        page.fill('[data-test="username"]', 'locked_out_user')

        page.wait_for_timeout(3000) 

        page.fill('[data-test="password"]', 'secret_sauce')

        page.wait_for_timeout(3000) 

        page.click('[data-test="login-button"]')

        page.wait_for_timeout(3000) 

        error_message = page.locator('[data-test="error"]')

        assert error_message.is_visible()

        browser.close()