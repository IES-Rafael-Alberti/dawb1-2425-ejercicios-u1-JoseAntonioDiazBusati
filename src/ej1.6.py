#
#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA
#que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
#
importe = float(input("Escribe el valor del importe: "))
iva = importe * (10/100)
articulo = importe - iva
print(f"El articulo cuesta: {articulo:.2f}")