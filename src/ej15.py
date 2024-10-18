"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año,
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años.
Redondear cada cantidad a dos decimales.
"""
capital = int(input("Ingrese la cantidad de dinero depositada: "))
interes = 4/100
anio1 = (capital * (1 + interes))
anio2 = (anio1 * (1 + interes))
anio3 = (anio2 * (1 + interes))
print("El primer año asciende a "+str("%.2f" % anio1)+", en el segundo año "+str("%.2f" %anio2)+" y por el tercer año "+str("%.2f" %anio3)+".")