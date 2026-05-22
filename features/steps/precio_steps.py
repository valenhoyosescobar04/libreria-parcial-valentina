import sys
from pathlib import Path

from behave import given, when, then

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from libreria.producto import Producto


@given('un producto llamado "{nombre}" con precio base {precio_base:g}')
def step_crear_producto(context, nombre, precio_base):
    context.producto = Producto(nombre=nombre, precio_base=precio_base)
    context.error = None
    context.resultado = None


@when("aplico un descuento de {descuento:g} por ciento")
def step_aplicar_descuento(context, descuento):
    context.resultado = context.producto.aplicar_descuento(descuento)


@when("intento aplicar un descuento de {descuento:g} por ciento")
def step_intentar_aplicar_descuento(context, descuento):
    try:
        context.producto.aplicar_descuento(descuento)
    except ValueError as error:
        context.error = str(error)


@when("calculo el precio final con descuento de {descuento:g} por ciento")
def step_calcular_precio_final(context, descuento):
    context.resultado = context.producto.calcular_precio_final(descuento)


@then("el precio con descuento debe ser {esperado:g}")
def step_validar_precio_con_descuento(context, esperado):
    assert context.resultado == esperado


@then('el sistema debe mostrar el error "{mensaje}"')
def step_validar_error(context, mensaje):
    assert context.error == mensaje


@then("el precio final debe ser {esperado:g}")
def step_validar_precio_final(context, esperado):
    assert context.resultado == esperado