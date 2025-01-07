"""
3. Escreva um programa que pede que o usuário dê entrada em dois valores, em seguida, exiba em tela o resultado da soma, subtração, multiplicação e divisão desses números:
"""

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

print(f"Soma: {n1:.2f} + {n2:.2f} = {(n1 + n2):.2f}")
print(f"Subtração 1: {n1:.2f} - {n2:.2f} = {(n1 - n2):.2f}")
print(f"Subtração 2: {n2:.2f} - {n1:.2f} = {(n2 - n1):.2f}")
print(f"Multiplicação: {n1:.2f} * {n2:.2f} = {(n1 * n2):.2f}")
print(f"Divisão 1: {n1:.2f} / {n2:.2f} = {(n1 / n2):.2f}")
print(f"Divisão 2: {n2:.2f} / {n1:.2f} = {(n2 / n1):.2f}")