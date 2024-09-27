"""
Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así
que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
"""
p_payaso = 112
p_muneca = 75
cant_payaso = int(input("Introduzca la cantidad de payasos vendidos: "))
cant_muneca = int(input("Introduzca la cantidad de muñecas vendidas: "))
peso_total = "%.2f"%(((p_muneca * cant_muneca) + (p_payaso * cant_payaso))/1000)
print("El paquete pesará: "+str(peso_total)+" kilogramos.")