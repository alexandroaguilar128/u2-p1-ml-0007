import numpy as np

print("---------- Llenar matriz de ceros ----------")
matriz = np.zeros([3,5]) # 3 filas x 5 columnas
print(matriz)
print("---------- Llenar matriz de unos ----------")
matriz = np.ones([3,5])
print(matriz)
print("---------- Llenar matriz vacios ----------")
matriz = np.empty([3,5])
print(matriz)
print("---------- Llenar lista con rangos ----------")
# El primer parametro es el valor incial
# El segundo parametro es el valor final
# El tercer parametro es el incremento
lista = np.arange(0, 10, 2)
print(lista)
print("---------- Llenar lista con rangos numero 2  ----------")
lista = np.arange(0, 10, 1)
print(lista)