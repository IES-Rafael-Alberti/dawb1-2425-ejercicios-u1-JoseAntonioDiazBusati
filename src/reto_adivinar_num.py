import random

objetivo = random.randint(0, 100)

num = int(input("Intenta adivinar un numero del 0 al 100: "))

while num != objetivo:
    if num > objetivo:
        dif = num - objetivo
        if dif <=10:
            print("Caliente caliente, estás cerca del objetivo")
        elif dif>=25:
            print("Frío frío, estás lejos del objetivo")
        else:
            print("El numero es mayor que el objetivo")
        num = int(input("Prueba otra vez: "))
    elif num < objetivo:
        dif = objetivo - num
        if dif <= 10:
            print("Caliente caliente, estás cerca del objetivo")
        elif dif >= 25:
            print("Frío frío, estás lejos del objetivo")
        else:
            print("El numero es menor que el objetivo")
        num = int(input("Prueba otra vez: "))
    else:
        print("Eso no es un numero")
        num = int(input("Prueba otra vez: "))