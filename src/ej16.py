"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante),
el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
"""
no_dia = int(input("Introduce las barras de pan vendidas que no son del día: "))
precio = 3.49
coste = (no_dia * 3.49)
descuento = (no_dia * 3.49)*60/100
print("El precio de una barra de pan es de "+str("%.2f" %precio)+"€, siendo la cantidad de barras que se ha comprado estas costaría: "+str("%.2f" %coste)+"€, pero como no son del día cuestan: "+str("%.2f" %descuento)+"€.")