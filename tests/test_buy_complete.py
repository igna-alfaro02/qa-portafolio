from playwright.sync_api import sync_playwright

def test_buy_complete_saucedemo():

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

        assert "inventory" in page.url

        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

        page.wait_for_timeout(3000)

        page.click('.shopping_cart_link')

        page.wait_for_timeout(3000)

        page.click('[data-test="checkout"]')

        page.wait_for_timeout(3000)

        page.fill('[data-test="firstName"]', 'Ignacio')

        page.fill('[data-test="lastName"]', 'QA')

        page.fill('[data-test="postalCode"]', '12345')

        page.click('[data-test="continue"]')

        page.wait_for_timeout(3000)

        page.click('[data-test="finish"]')

        page.wait_for_timeout(3000)

        confirmation = page.locator('.complete-header')

        assert confirmation.inner_text() == "Thank you for your order!"

        page.screenshot(path="screenshots/TC-CHECKOUT-002_evidencia_saucedemo.png")

        page.wait_for_timeout(3000)

        browser.close()
