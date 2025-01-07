"""
18. Crie um programa que realiza a progressão aritimética de n elementos, com o primeiro termo, a razão e a quantidade n de elementos definidos pelo usuário.
Desafio: Armazene a PA em uma lista.
"""

a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
n = int(input("Digite a quantidade de elementos: "))

# pa = a1 + (n - 1) * r

# for i in range(a1, pa + r, r):
#     print(i)

# Código para o desafio:

pa = []

for i in range(n):
    termo = a1 + i * r
    pa.append(termo)

print(f"PA = {pa}")