import random

def pedirnumero():
    return int(input("\nIntenta adivinar un numero del 0 al 100: "))

def comprobar_numero():
    num = pedirnumero()
    while num >=0 or num <= 100:
        if num <0:
            print("Sólo puedes introducir de 0 al 100!!!\n")
            num = pedirnumero()
        elif num >100:
            print("Sólo puedes introducir de 0 al 100!!!\n")
            num = pedirnumero()
        else:
            return num


def diferencial(objetivo: random, numero: int):
    if objetivo > numero:
        return objetivo-numero
    elif objetivo < numero:
        return numero-objetivo


def main():
    objetivo = random.randint(0, 100)
    intentos = 1
    assist = False
    while not assist:
        numero = comprobar_numero()
        dif = diferencial(objetivo, numero)
        if numero > objetivo:
            if dif <= 3:
                print("Te estás quemando, el objetivo está muy cerca.")
            elif dif <= 10:
                print("Caliente caliente, estás cerca del objetivo.")
            elif dif >= 25:
                print("Frío frío, estás lejos del objetivo.")
            else:
                print("El numero es mayor que el objetivo.")
            intentos += 1
        elif numero < objetivo:
            if numero < objetivo:
                if dif <= 3:
                    print("Te estás quemando, el objetivo está muy cerca.")
                elif dif <= 10:
                    print("Caliente caliente, estás cerca del objetivo.")
                elif dif >= 25:
                    print("Frío frío, estás lejos del objetivo.")
                else:
                    print("El numero es menor que el objetivo.")
            intentos += 1
        else:
            print("\nLO HAS CONSEGUIDO!!!")
            assist = True
    print("Has superado el reto en", intentos, "intentos.")


if __name__ == "__main__":
    main()