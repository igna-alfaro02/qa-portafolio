from playwright.sync_api import sync_playwright

def test_add_product_to_cart():

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

        page.wait_for_timeout(3000) 

        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

        page.wait_for_timeout(3000) 

        cart_badge = page.locator('.shopping_cart_badge')

        assert cart_badge.inner_text() == "1"

        browser.close()