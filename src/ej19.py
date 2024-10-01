"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y
n es el número de letras que tienen el nombre.
"""
nombre = input("Introduce un nombre: ")
n = len(nombre)
print(nombre.upper()+" es el nombre de usuario en mayusculas y "+str(n)+" es el numero de letras.")