Feature: Calcular precio final de productos de la librería
  Como administrador de la Librería del Centro
  quiero aplicar descuentos válidos y calcular el precio final con IVA
  para vender productos con reglas claras y precios correctos.

  Background:
    Given un producto llamado "Libro" con precio base 100000

  @descuento @positivo
  Scenario Outline: Aplicar descuentos válidos al producto
    When aplico un descuento de <descuento> por ciento
    Then el precio con descuento debe ser <precio_con_descuento>

    Examples:
      | descuento | precio_con_descuento |
      | 0         | 100000               |
      | 20        | 80000                |
      | 40        | 60000                |

  @descuento @error
  Scenario: Rechazar descuento mayor al cuarenta por ciento
    When intento aplicar un descuento de 41 por ciento
    Then el sistema debe mostrar el error "El descuento debe estar entre 0% y 40%"

  @descuento @error
  Scenario: Rechazar descuento negativo
    When intento aplicar un descuento de -1 por ciento
    Then el sistema debe mostrar el error "El descuento debe estar entre 0% y 40%"

  @precio_final @positivo
  Scenario: Calcular precio final aplicando primero descuento y luego IVA
    When calculo el precio final con descuento de 10 por ciento
    Then el precio final debe ser 107100

  @precio_final @borde
  Scenario: Calcular precio final sin descuento
    When calculo el precio final con descuento de 0 por ciento
    Then el precio final debe ser 119000

  @precio_final @borde
  Scenario: Calcular precio final con descuento máximo permitido
    When calculo el precio final con descuento de 40 por ciento
    Then el precio final debe ser 71400