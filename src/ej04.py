"""
Escribe un programa que le pida al usuario una temperatura en grados Celsius,
la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
"""
celsius = int(input("Ingrese el temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 /5) + 32
print("La temperatura convertida es: "+str(fahrenheit)+"Fº.")