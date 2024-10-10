"""
Realiza un programa en Python que solicite un nombre y una edad.
Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que
introduzca una edad comprendida entre 0 y 125 años. El programa mostrará la siguiente frase:
"Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
"""
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
while edad < 0 or edad > 125:
    print("Edad no valida!!!")
    edad = int(input("Vuelve a introducir tu edad: "))
if nombre == "":
    print("Te llamas Desconocido y tienes "+str(edad)+" años, te quedan "+str(125-edad)+" años por cumplir.")
else:
    print("Te llamas "+nombre+" y tienes "+str(edad)+" años, te quedan "+str(125-edad)+" años por cumplir.")