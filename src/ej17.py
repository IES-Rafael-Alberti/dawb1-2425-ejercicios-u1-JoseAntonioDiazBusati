"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nombre = input("Ingrese el nombre del usuario: ")
num = int(input("Introduzca un numero entero: "))
repetir = (nombre+"\n")* num
print(repetir)