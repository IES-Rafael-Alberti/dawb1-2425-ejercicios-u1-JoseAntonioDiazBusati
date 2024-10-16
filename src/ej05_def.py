"""
Escribe un programa que pida el importe sin IVA de un artículo y
el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

Recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada,
sino que se imprime desde dentro de la función.
"""

def importe_articulo():
    return float(input("Introduce el importe del articulo sin IVA: "))

def importe_iva():
    return float(input("Introduce el IVA de dicho articulo: "))

def precio():
    articulo = importe_articulo()
    iva = importe_iva()
    return articulo + (articulo * iva / 100)

def main():
    resultado = precio()
    print(f"El precio final del artículo con IVA es: {resultado:.2f} euros")

if __name__ == "__main__":
    main()