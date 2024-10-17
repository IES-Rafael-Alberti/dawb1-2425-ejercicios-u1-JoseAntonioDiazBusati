"""
Escribe un programa para pedirle al usuario las horas de trabajo y
el precio por hora y calcule el importe total del servicio.
"""
def horas():
    hora = int(input("Introduce las horas de trabajo: "))
    return hora

def coste():
    costes = float(input("Introduce el coste por hora: "))
    return costes

def importe(horas_total, coste_total):
    importe_total = horas_total * coste_total
    return importe_total

def main():
   print(importe(horas(), coste()))

if __name__ == '__main__':
    main()