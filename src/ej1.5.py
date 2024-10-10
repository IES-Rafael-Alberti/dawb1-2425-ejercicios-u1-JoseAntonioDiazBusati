#
#Escribe un programa que pida el importe sin IVA de un artículo y
#el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
#
articulo = float(input("Introduzca el importe sin IVA de un articulo: "))
iva = float(input("Introduzca el IVA de ese articulo: "))
precio = ((iva * articulo) / 100) + articulo
print(f"El precio del articulo es: {precio:.2f}.")