import os
os.system("cls")

#7 - Convertir datos de tipo texto a entero

Precio1 = int(input("Introduzca el precio: "))
Precio2 = int(input("Introduzca su precio: "))

Total = Precio1 + Precio2
#Se utiliza f para poder imprimir el entero en un texto
#Se encierra la variable entera en {} para poder imprimirla
print(f"El precio total es: {Total}")