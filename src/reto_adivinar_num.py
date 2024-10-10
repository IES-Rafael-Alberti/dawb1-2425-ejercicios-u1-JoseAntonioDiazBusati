import random

objetivo = random.randint(0, 100)

num = int(input("Intenta adivinar un numero del 0 al 100: "))
contador = 5

while num != objetivo or contador >= 0:
    if num > objetivo:
        print("El numero es mayor que el objetivo")
        contador -= 1
        num = int(input("Intenta adivinar un numero del 0 al 100: "))
    elif num < objetivo:
        print("El numero es menor que el objetivo")
        contador -= 1
        num = int(input("Intenta adivinar un numero del 0 al 100: "))
    else:
        print("El numero es igual que el objetivo")