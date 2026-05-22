# Librería Parcial - Pruebas de Software

Autor	Valentina Hoyos Escobar

Este proyecto implementa un módulo para calcular el precio final de productos de la Librería del Centro, aplicando validaciones sobre precio base, descuento porcentual e IVA.

## Tecnologías usadas

- Python
- pytest
- pytest-cov
- behave

---

# Parte 1 - Análisis inicial

## Regla 1: Producto con nombre y precio base mayor que cero

Un producto debe tener nombre y precio base. El precio base debe ser mayor que cero. Si el precio base es cero o negativo, el sistema debe rechazarlo con un mensaje claro.

### Particiones de equivalencia - Regla 1

| Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Precio base mayor que cero | Válida | 10000 | Producto creado correctamente |
| Precio base igual a cero | Inválida | 0 | Rechazar con mensaje claro |
| Precio base menor que cero | Inválida | -5000 | Rechazar con mensaje claro |

---

## Regla 2: Descuento porcentual entre 0% y 40%

El descuento debe estar entre 0% y 40%. Un descuento mayor al 40% debe ser rechazado. El descuento de 0% es válido.

### Particiones de equivalencia - Regla 2

| Partición | Tipo | Valor representativo | Resultado esperado |
|---|---|---:|---|
| Descuento entre 0% y 40% | Válida | 20 | Aplicar descuento correctamente |
| Descuento igual a 0% | Válida | 0 | No aplicar descuento, pero aceptar el valor |
| Descuento igual a 40% | Válida | 40 | Aplicar descuento máximo permitido |
| Descuento menor que 0% | Inválida | -1 | Rechazar con mensaje claro |
| Descuento mayor que 40% | Inválida | 41 | Rechazar con mensaje claro |

### Análisis de valores límite - Regla 2

| Valor | Tipo | Resultado esperado |
|---:|---|---|
| -1 | Fuera del límite inferior | Rechazar |
| 0 | Límite inferior válido | Aceptar |
| 1 | Justo encima del límite inferior | Aceptar |
| 39 | Justo debajo del límite superior | Aceptar |
| 40 | Límite superior válido | Aceptar |
| 41 | Fuera del límite superior | Rechazar |

---

## Regla 3: Precio final con descuento e IVA

El precio final se calcula aplicando primero el descuento y luego el IVA del 19% sobre el resultado. El precio final nunca puede ser negativo.

### Pregunta para el administrador

¿El precio final debe redondearse a dos decimales o debe conservar todos los decimales del cálculo?

Justificación: Esta información es importante porque al aplicar porcentajes pueden aparecer decimales y el sistema debe manejar los precios de forma consistente.

---

# Parte 2 - Casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP-01 | Regla 1 | Crear producto con precio base válido | No existe producto creado | nombre: "Libro", precio: 10000 | Crear producto | El producto se crea correctamente | Positivo |
| CP-02 | Regla 1 | Rechazar producto con precio base cero | No existe producto creado | nombre: "Libro", precio: 0 | Crear producto | El sistema rechaza el producto con mensaje claro | Borde |
| CP-03 | Regla 1 | Rechazar producto con precio base negativo | No existe producto creado | nombre: "Libro", precio: -5000 | Crear producto | El sistema rechaza el producto con mensaje claro | Negativo |
| CP-04 | Regla 2 | Aplicar descuento normal | Producto creado con precio 100000 | descuento: 20 | Aplicar descuento | El precio con descuento queda en 80000 | Positivo |
| CP-05 | Regla 2 | Aceptar descuento mínimo | Producto creado con precio 100000 | descuento: 0 | Aplicar descuento | El precio se mantiene en 100000 | Borde |
| CP-06 | Regla 2 | Aceptar descuento máximo permitido | Producto creado con precio 100000 | descuento: 40 | Aplicar descuento | El precio con descuento queda en 60000 | Borde |
| CP-07 | Regla 2 | Rechazar descuento mayor al permitido | Producto creado con precio 100000 | descuento: 41 | Aplicar descuento | El sistema rechaza el descuento con mensaje claro | Negativo |
| CP-08 | Regla 2 | Rechazar descuento negativo | Producto creado con precio 100000 | descuento: -1 | Aplicar descuento | El sistema rechaza el descuento con mensaje claro | Negativo |
| CP-09 | Regla 3 | Calcular precio final con descuento e IVA | Producto creado con precio 100000 | descuento: 10, IVA: 19% | Calcular precio final | El precio final queda en 107100 | Positivo |
| CP-10 | Regla 3 | Calcular precio final sin descuento | Producto creado con precio 100000 | descuento: 0, IVA: 19% | Calcular precio final | El precio final queda en 119000 | Borde |
| CP-11 | Regla 3 | Calcular precio final con descuento máximo | Producto creado con precio 100000 | descuento: 40, IVA: 19% | Calcular precio final | El precio final queda en 71400 | Borde |

---

# Reporte de cobertura

Comando usado:

```bash
pytest --cov=src --cov-report=term-missing

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
src/libreria/__init__.py       0      0   100%
src/libreria/producto.py      22      0   100%
--------------------------------------------------------
TOTAL                         22      0   100%gi