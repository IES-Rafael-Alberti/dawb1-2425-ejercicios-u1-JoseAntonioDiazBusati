"""
Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error
o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción
es más fácil, aunque el mundo está lleno de valientes).
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente
lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
"""

inicio = int(input("Introduce el numero de inicio de una serie: "))

incremento = int(input("Introduce el numero de incremento de una serie: "))
while incremento <=0:
    print("No puede ser 0 o menos. Intentalo de nuevo!!")
    incremento = int(input("Vuelve a introducir el numero de incremento de la serie: "))

total = int(input("Introduce el total de la serie: "))
while total <= 0:
    print("No puede ser 0 o menos. Intentalo de nuevo!!")
    total = int(input("Vuelve a introducir el total de la serie: "))

for inicio in range(inicio,total+1):
    print(inicio)
    inicio += incremento
