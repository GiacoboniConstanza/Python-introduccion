import os
os.system("cls")

def promedioNotas(Nota1, Nota2, Nota3):
    promedio = (Nota1+Nota2+Nota3)/3
    return promedio

prom = promedioNotas(9,7,8)
print(prom)