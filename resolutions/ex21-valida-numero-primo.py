"""
21. Crie um programa que pede ao usuário um número qualquer e em seguido retorne se esse número é primo ou não.
"""

numero = int(input("Digite um número: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{numero} é um número primo!")
else:
    print(f"{numero} não é um número primo pois possui {divisores} divisores.")