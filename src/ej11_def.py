"""
Escribir un programa que lea un entero positivo, n, introducido por
el usuario y después muestre en pantalla la suma de todos
los enteros desde 1 hasta n. La suma de los n
primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2

Recibe un número y retorna una cadena de caracteres con el resultado de la función.
"""
def pedir_num():
    entero = int(input("Introduce  un numero entero: "))
    return entero

def suma_entero():
    n = pedir_num()
    suma = n * (n + 1) / 2
    return suma

def main():
    suma = suma_entero()
    print("La suma de los numeros enteros es: "+str(suma))

if __name__ == "__main__":
    main()