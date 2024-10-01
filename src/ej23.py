"""
Escribir un programa que pregunte el correo electrónico
del usuario en la consola y muestre por pantalla otro
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
correo = input("Introduzca su correo electronico: ")
separacion = correo.split("@")[0].split(":")[0]
print(separacion+"@ceu.es")