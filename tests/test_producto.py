import pytest

from libreria.producto import Producto


# Regla 1: Producto con precio base mayor que cero

def test_crear_producto_con_precio_base_valido():
    producto = Producto(nombre="Libro", precio_base=10000)

    assert producto.nombre == "Libro"
    assert producto.precio_base == 10000


def test_rechazar_producto_con_precio_base_cero():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto(nombre="Libro", precio_base=0)


def test_rechazar_producto_con_precio_base_negativo():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto(nombre="Libro", precio_base=-5000)


# Regla 2: Descuento entre 0% y 40%

def test_aplicar_descuento_normal():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_con_descuento = producto.aplicar_descuento(20)

    assert precio_con_descuento == 80000


def test_aceptar_descuento_minimo_cero():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_con_descuento = producto.aplicar_descuento(0)

    assert precio_con_descuento == 100000


def test_aceptar_descuento_maximo_cuarenta():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_con_descuento = producto.aplicar_descuento(40)

    assert precio_con_descuento == 60000


def test_rechazar_descuento_mayor_a_cuarenta():
    producto = Producto(nombre="Libro", precio_base=100000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(41)


def test_rechazar_descuento_negativo():
    producto = Producto(nombre="Libro", precio_base=100000)

    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(-1)


# Regla 3: Precio final aplicando descuento y luego IVA

def test_calcular_precio_final_con_descuento_e_iva():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_final = producto.calcular_precio_final(10)

    assert precio_final == 107100


def test_calcular_precio_final_sin_descuento():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_final = producto.calcular_precio_final(0)

    assert precio_final == 119000


def test_calcular_precio_final_con_descuento_maximo():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_final = producto.calcular_precio_final(40)

    assert precio_final == 71400


def test_precio_final_nunca_es_negativo():
    producto = Producto(nombre="Libro", precio_base=100000)

    precio_final = producto.calcular_precio_final(40)

    assert precio_final >= 0