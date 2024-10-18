"""Escribe un programa que pida el nombre del usuario para luego darle la bienvenida."""

def saludar(name):
    return f"Hola, {name}"

def main():
    nombre = input("Ingrese el nombre del usuario: ")
    print(saludar(nombre))

if __name__ == '__main__':
    main()