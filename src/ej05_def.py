"""
Escribe un programa que pida el importe sin IVA de un artículo y
el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

Recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
"""
articulo = int(input("Introduzca el importe sin IVA de un articulo: "))
iva = int(input("Introduzca el IVA de ese articulo: "))
precio = ((iva * articulo) / 100) + articulo
print("El precio del articulo es: ", precio)

