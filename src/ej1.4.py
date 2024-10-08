#
#Formatear la salida de los grados Farenheit a dos posiciones decimales.
#Mostrar en pantalla:
#La temperatura en grados Farenheit es 0.00ºF (0.00ºC)
#
celsius = float(input("Ingrese el temperatura en grados Celsius: "))
fahrenheit = (celsius * 9 /5) + 32
print(f"La temperatura convertida es: {fahrenheit:.2f} Fº.")