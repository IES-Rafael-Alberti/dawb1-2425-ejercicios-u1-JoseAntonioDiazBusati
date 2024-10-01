"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS:
"la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos
por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
"""
n = int(input("Indica un numero cualquiera: "))
m = int(input("Indica otro numero cualquiera: "))
c = n // m
r = n % m
print("A partir de esos 2 numeros salen: "+str(c)+" como su cociente y "+str(r)+" como su resto")