#Pedir un numero entero
#con control de excepciones

def comprobar_entero(string):
    string = string.strip()
    return string.isdigit() or (string.startswith('-') and string[1:].isdigit())

def pedir_entero():
    string = input("Introduce un numero entero: ")
    while not comprobar_entero(string):
        string = input("***ERROR*** Eso no es un numero entero!!!\n\nIntroduce un numero entero otra vez: ")
    return int(string)

def main():
    num = pedir_entero()
    print(f"Has introducido el numero: {num}")

if __name__ == '__main__':
    main()