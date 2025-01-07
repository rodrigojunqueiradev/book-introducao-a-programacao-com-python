"""
19. Desenvolva um código que exiba em tela a tabuada de um número fornecido pelo usuário:
"""

num = int(input("Digite o número: "))
final = int(input("Quer calcular a tabuada até qual fator? "))

for i in range(1, final + 1):
    print(f"{num} x {i} = {num*i}")