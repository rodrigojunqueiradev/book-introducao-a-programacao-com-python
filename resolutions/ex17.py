"""
17. Crie um programa que exiba a contagem de 0 a 20 exibindo apenas os número pares.
"""

# Forma 1: 
for i in range(0,21):
    if i % 2 == 0:
        print(i)

# Forma 2:
for i in range(0,21,2):
    print(i)