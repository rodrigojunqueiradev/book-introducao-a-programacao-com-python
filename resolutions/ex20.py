"""
20. Crie um programa que realize a contagem de 1 até 100 usando apenas número ímpares, ao final do processo exiba em tela quantos números ímpares foram encontrados nesse intervalo, assim como a soma deles.
"""

soma_impares = 0
quantidade_impares = 0

for i in range(0,101):
    if i % 2 != 0:
        soma_impares += i
        quantidade_impares += 1

print(f"A soma dos números ímpares é: {soma_impares}")
print(f"Foram contato {quantidade_impares} números ímpares.")