import pytest

from libreria.producto import Producto


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