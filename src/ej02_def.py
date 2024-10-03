"""
Escribe un programa para pedirle al usuario las horas de trabajo y
el precio por hora y calcule el importe total del servicio.
"""
def horas():
    return int(input("Introduce las horas de trabajo: "))

def coste():
    return float(input("Introduce el coste por hora: "))

def importe(importe):
    print("Importe total: "+str(importe))

def main():
    horas_total = horas()
    coste_total = coste()
    importe_total = horas_total * coste_total
    importe(importe_total)

if __name__ == '__main__':
    main()