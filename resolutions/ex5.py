"""
5. Crie duas variáveis com dois valores numéricos inteiros digitados pelo usuário, caso o valor do primeiro número foi maior que o do segundo, exiba em tela uma mensagem de acordo, caso contrário, exiba em tela uma mensagem dizendo o primeiro valor digitado é menor que o segundo.
"""

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
else:
    print(f"{n1} é menor ou igual a {n2}")