"""Escribe un programa que pida el nombre del usuario para luego darle la bienvenida."""

def saludar(nombre):
    print("Hola, "+nombre+".")
def main():
    saludar(input("Ingrese su nombre"))
if __name__ == '__main__':
    main()