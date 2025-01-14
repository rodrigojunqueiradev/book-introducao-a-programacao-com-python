"""
33. Faça um rograma que leia duas listas e que gere uma terceira lista com os elementos das duas primeiras. Exiba a nova lista.
"""

lista1 = []
lista2 = []

quantidade_elementos = int(input("Quantos elementos vão ter cada lista? "))
x = 0

while x < quantidade_elementos:
    item1 = input(f"Informe o elemento {x + 1} da lista 1: ")
    lista1.append(item1)
    item2 = input(f"Informe o elemento {x + 1} da lista 2: ")
    lista2.append(item2)
    x += 1

lista3 = lista1 + lista2
print(lista3)