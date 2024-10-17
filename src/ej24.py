"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
precios = float(input("Ingrese el precio del producto: "))
precio = str("%.2f" % precios)
euro = precio.split(".")[0]
centimo = precio.split(".")[1]
print("El precio del producto es de "+euro+" euros y de "+centimo+" centimos.")