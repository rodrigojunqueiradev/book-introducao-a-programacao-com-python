"""
16. Desenvolva um programa que solicite um valor de início e um valor de fim, exibindo em tela a contagem dos números dentro desse intervalo.
"""

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))

for i in range(inicio, fim + 1):
    print(i)
