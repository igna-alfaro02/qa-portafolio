# DemoBlaze — Testing Manual

Proyecto de QA manual funcional sobre [DemoBlaze](https://www.demoblaze.com), una tienda online de práctica.

## Herramientas

- Testing manual funcional
- Documentación en Excel (plan de pruebas, suites y casos)
- Capturas de pantalla como evidencia por caso

## Documentación

El archivo [`Demoblaze QA Manual Portafolio.xlsx`](./Demoblaze%20QA%20Manual%20Portafolio.xlsx) contiene:

- **Test Plan** — alcance, objetivos y criterios de aceptación
- **Test Suites** — agrupación de casos por funcionalidad
- **Test Cases** — pasos, datos de entrada y resultado esperado

## Casos de prueba

| ID | Funcionalidad | Descripción |
|----|--------------|-------------|
| TC-LOGIN-002 | Login | Login con credenciales válidas |
| TC-LOGIN-003 | Login | Login con credenciales inválidas |
| TC-REG-001 | Registro | Registro de nuevo usuario |
| TC-REG-002 | Registro | Registro con datos duplicados |
| TC-PDP-001 | Producto | Visualización de detalle de producto |
| TC-PDP-002 | Producto | Navegación entre categorías de producto |
| TC-CART-001 | Carrito | Agregar producto al carrito |
| TC-CART-002 | Carrito | Eliminar producto del carrito |
| TC-CHECKOUT-001 | Checkout | Completar compra con datos válidos |
| TC-CHECKOUT-002 | Checkout | Checkout con campos vacíos |
| TC-CONTACT-001 | Contacto | Envío de formulario de contacto |
| TC-CONTACT-002 | Contacto | Envío de formulario sin datos |
| TC-CAT-001 | Categorías | Filtrar productos por categoría |
| TC-CAT-002 | Categorías | Verificar productos listados por categoría |

## Evidencias

Las capturas de pantalla de cada caso se encuentran en la carpeta [`screenshots/`](./screenshots/).
