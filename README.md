# Portfolio QA — Ignacio Alfaro

Portfolio de QA con dos proyectos de formación práctica. Cubre automatización de pruebas con Playwright y testing manual funcional.

| Proyecto | Tipo | Herramientas |
|----------|------|--------------|
| [SauceDemo](#saucedemo--automatización) | Automatización | Python, Playwright, pytest |
| [DemoBlaze](./test-demoblaze/README.md) | Manual | Testing funcional, Excel |

---

## SauceDemo — Automatización

Automatización de pruebas funcionales sobre [SauceDemo](https://www.saucedemo.com), una aplicación de e-commerce de práctica.

### Herramientas

- Python 3.x
- Playwright (sync API)
- pytest

### Casos de prueba

| ID | Descripción | Archivo |
|----|-------------|---------|
| TC-LOGIN-001 | Login exitoso con credenciales válidas | `test_login.py` |
| TC-LOGIN-002 | Login con usuario bloqueado | `test_login_fail.py` |
| TC-HOME-001 | Verificación del título de la homepage | `test_homepage.py` |
| TC-CART-001 | Agregar producto al carrito | `test_add_cart.py` |
| TC-CART-002 | Validar producto en el carrito | `test_cart_validation.py` |
| TC-CHECKOUT-001 | Flujo de compra completo | `test_buy_complete.py` |
| TC-E2E-001 | Flujo end-to-end de checkout | `test_e2e_checkout.py` |

### Evidencias

Las capturas de pantalla de cada ejecución se encuentran en la carpeta [`screenshots/`](./screenshots/).

### Cómo ejecutar

**1. Instalar dependencias:**

```bash
pip install -r requirements.txt
playwright install chromium
```

**2. Ejecutar todos los tests:**

```bash
pytest
```

**3. Ejecutar un test específico:**

```bash
pytest tests/test_login.py
```

Los tests se ejecutan en modo visual (headless=False) para facilitar la revisión de la ejecución.

---

## Estructura del repositorio

```
qa-portafolio/
├── tests/                  # Scripts de automatización (SauceDemo)
├── screenshots/            # Evidencias de ejecución (SauceDemo)
├── test-demoblaze/         # Proyecto de testing manual (DemoBlaze)
├── requirements.txt
├── pytest.ini
└── README.md
```
