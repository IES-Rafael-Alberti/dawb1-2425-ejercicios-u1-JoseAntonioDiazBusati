#Desarrolla una funcion que pida 2 numeros y que retorne el numero mayor o 0 si son iguales.

def pedir_num():
    num = int(input("Ingrese un numero: "))
    return num

def comparar_num(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return 0

def main():
    comparar_num(pedir_num(),pedir_num())

if __name__ == '__main__':
    main()