"""
Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y
cuántos números existen entre ellos dos. El segundo número no puede ser igual, si es así,
debe mostrar el error: "Los números no pueden ser iguales". Si los números son diferentes,
por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".
"""
num1 = int(input("Introduce un numero cualquiera: "))
num2 = int(input("Introduce otro numero cualquiera: "))
if num1 > num2:
    print("El numero menor es el "+str(num2)+" y entre ellos existen "+str((num1-num2))+" numeros enteros.")
elif num2 > num1:
    print("El numero menor es el "+str(num1)+" y entre ellos existen "+str((num2-num1))+" numeros enteros.")
else:
    print("No pueden ser iguales!!!")