from playwright.sync_api import sync_playwright

def test_complete_checkout_flow():

    with sync_playwright() as p:

        # Abrir navegador
        browser = p.chromium.launch(headless=False)

        # Crear página
        page = browser.new_page()

        # Ir a SauceDemo
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill('[data-test="username"]', 'standard_user')

        page.fill('[data-test="password"]', 'secret_sauce')

        page.click('[data-test="login-button"]')    

        # Validar login exitoso
        assert "inventory" in page.url

        # Agregar producto
        page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

        # Validar carrito = 1
        cart_badge = page.locator('.shopping_cart_badge')

        assert cart_badge.inner_text() == "1"

        # Ir carrito
        page.click('.shopping_cart_link')

        # Validar producto carrito
        product_name = page.locator('.inventory_item_name')

        assert product_name.inner_text() == "Sauce Labs Backpack"

        # Checkout
        page.click('[data-test="checkout"]')

        # Completar formulario
        page.fill('[data-test="firstName"]', 'Ignacio')

        page.fill('[data-test="lastName"]', 'QA')

        page.fill('[data-test="postalCode"]', '12345')

        # Continuar
        page.click('[data-test="continue"]')

        # Validar página overview
        assert "checkout-step-two" in page.url

        # Finalizar compra
        page.click('[data-test="finish"]')

        # Validar compra exitosa
        confirmation = page.locator('.complete-header')

        assert confirmation.inner_text() == "Thank you for your order!"

        # Screenshot final
        page.screenshot(path="screenshots/e2e_checkout_success.png")

        # Espera visual opcional
        page.wait_for_timeout(3000)

        # Cerrar navegador
        browser.close()