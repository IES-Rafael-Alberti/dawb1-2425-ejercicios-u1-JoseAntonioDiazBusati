"""
Escribe un programa para pedirle al usuario las horas de trabajo y
el precio por hora y calcule el importe total del servicio.
"""
horas = int(input("Horas de trabajo: "))
coste = int(input("Coste por hora: "))
print("Importe: "+str(horas*coste))