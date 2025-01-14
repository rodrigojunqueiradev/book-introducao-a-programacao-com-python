"""
34. Faça um programa que percorra duas listas com números e gere uma terceira sem elementos repetidos.
lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 10, 100, 1000]
"""

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 10, 100, 1000]
lista3 = []
lista_combinada = lista1 + lista2

for item in lista_combinada:
    if (item in lista1 and item not in lista2) or (item in lista2 and item not in lista1):
        lista3.append(item)

lista3.sort()
print(lista3)