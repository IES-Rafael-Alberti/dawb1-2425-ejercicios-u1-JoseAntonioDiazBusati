"""
Escribe un programa que le pida al usuario una temperatura en grados Celsius,
la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius
y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales.
Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.

"""
def pedir_fahrenheit():
    return float(input("Introduce la temperatura en grados Fahrenheit: "))

def pedir_grados():
    fahrenheit = pedir_fahrenheit()
    celsius = (fahrenheit - 32) * 5/9
    return f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"

def main():
    pedir_grados()