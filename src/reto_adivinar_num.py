import random
"""
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
"""
def pedirnumero():
    return int(input("Intenta adivinar un numero del 0 al 100: "))

def comprobar_numero():
    num = pedirnumero()
    while num >=0 or num <= 100:
        if num <0:
            print("Sólo puedes introducir de 0 al 100!!!")
            num = pedirnumero()
        elif num >100:
            print("Sólo puedes introducir de 0 al 100!!!")
            num = pedirnumero()
        else:
            return num

"""
def diferencial():
"""

def main():
    objetivo = random.randint(0, 100)
    intentos = 1
    assist = False
    while not assist:
        numero = comprobar_numero()
        if numero > objetivo:
            print("El numero es mayor que el objetivo")
            intentos += 1
        elif numero < objetivo:
            print("El numero es menor que el objetivo")
            intentos += 1
        else:
            print("LO HAS CONSEGUIDO!!!")
            assist = True
    print("Has superado el reto en", intentos, "intentos")


if __name__ == "__main__":
    main()