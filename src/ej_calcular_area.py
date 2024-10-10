import math

def calcular_area(a: float, b: float, c: float) -> float:
    semiperimetro = (a + b + c)/2
    area = math.sqrt(semiperimetro * (semiperimetro-a) * (semiperimetro-b) * (semiperimetro-c))
    return area

def comprobar_float(valor: str) -> bool:
    if valor.startswith("-"):
        valor = valor[1:]

    pos_punto = valor.find(".")

    if pos_punto >= 0:
        valor = valor[:pos_punto] + valor[pos_punto+1:]

    return valor.isdigit()

def introducir_numero(msj: str) -> float:
    valor = input("\n" + msj).strip().replace(",", ".")

    valor.startswith("-")

    while not comprobar_float(valor):
        print("***ERROR***\nNumero invalido!!!")
        valor = input("\n" + msj).strip().replace(",", ".")

    return float(valor)

def comprobar_triangulo(a, b, c):
    return (a+b>c) and (b+c>a) and (c+a>b)

def main():
    print("Dame los tres lados del triangulo...")

    lado_a = introducir_numero("Ingrese el lado 1 del triangulo: ")
    lado_b = introducir_numero("Ingrese el lado 2 del triangulo: ")
    lado_c = introducir_numero("Ingrese el lado 3 del triangulo: ")

    if comprobar_triangulo(lado_a, lado_b, lado_c):
        area = calcular_area(lado_a, lado_b, lado_c)
        print("\nEl area del triangulo con lados ({:.2f},{:.2f},{:.2f}) es {:.2f}".format(lado_a, lado_b, lado_c, area))
    else:
        print("\nEl area del triangulo con lados ({:.2f},{:.2f},{:.2f}) no es válido!!!".format(lado_a, lado_b, lado_c))

if __name__ == '__main__':
    main()