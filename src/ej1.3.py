#Analizar las siguientes expresiones:
#   ancho / alto
#   ancho // 2
#   ancho / 2
#   ancho * 2
#   ancho * alto
#   (5 + 1) * 3
#   (5 + 1) / 3
#Después, mostrar el resultado y el tipo por pantalla de cada expresión para comprobar si habéis acertado.
#La salida esperada es:
#   ancho / alto = 1.4166666666666667 y es de tipo <class 'float'>

ancho = 17
alto = 12.0

tipo1 = type(ancho/alto) # Tipo de dato: float, resultado = 1.4166666666666667.
tipo2 = type(ancho//2) # Tipo de dato: int, resultado = 8.
tipo3 = type(ancho/2) # Tipo de dato: float, resultado = 8.5.
tipo4 = type(ancho*2) # Tipo de dato: int, resultado = 34.
tipo5 = type(ancho*alto) # Tipo de dato: float, resultado = 204.0.
tipo6 = type((5+1)*3) # Tipo de dato: int, resultado = 18.
tipo7 = type((5+1)/3) # Tipo de dato: float, resultado = 2.0.

print("Tipo de dato: ",tipo1,", resultado = ",(ancho/alto),"\nTipo de dato: ",tipo2,", resultado = ",(ancho//2),"\nTipo de dato: "
      ,tipo3,", resultado = ",(ancho/2),"\nTipo de dato: ",tipo4,", resultado = ",(ancho*2),"\nTipo de dato: ",tipo5,", resultado = ",(ancho*alto),
      "\nTipo de dato: ",tipo6,", resultado = ",((5+1)*3),"\nTipo de dato: ",tipo7,", resultado = ",((5+1)/3))