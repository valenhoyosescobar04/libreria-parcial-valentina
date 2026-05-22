class Producto:
    def __init__(self, nombre: str, precio_base: float):
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")

        self.nombre = nombre
        self.precio_base = precio_base

    def aplicar_descuento(self, descuento: float) -> float:
        if descuento < 0 or descuento > 40:
            raise ValueError("El descuento debe estar entre 0% y 40%")

        return self.precio_base * (1 - descuento / 100)

    def calcular_precio_final(self, descuento: float) -> float:
        precio_con_descuento = self.aplicar_descuento(descuento)
        return precio_con_descuento * 1.19