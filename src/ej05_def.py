"""
Escribe un programa que pida el importe sin IVA de un artículo y
el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
"""
articulo = int(input("Introduzca el importe sin IVA de un articulo: "))
iva = int(input("Introduzca el IVA de ese articulo: "))
precio = ((iva * articulo) / 100) + articulo
print("El precio del articulo es: ", precio)

