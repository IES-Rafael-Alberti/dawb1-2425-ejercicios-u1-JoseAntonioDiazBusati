"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable,
y muestre por pantalla la frase Tu índice de masa corporal es donde
es el índice de masa corporal calculado redondeado con dos decimales.
"""
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))
imc = (peso / (altura * altura))
resultado = "%.2f" % imc
print("Su IMC es de "+str(resultado))