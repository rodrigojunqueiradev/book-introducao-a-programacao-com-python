"""
31. Escreva um programa para uma calculadora com as 4 operações matemática básicas e a opção de "Sair".
O usuário poderá utilizar a calcular até que a opção de "Sair" seja selecionada.
"""

print("Bem-vindo a calculadora Calculando")

sair = True

while sair:
    operacao = input("Informe a operação: \n(+ para Soma; - para Diferença; * para Multiplicação; / para Divisão; S- Sair) ").lower()

    if operacao == "s":
        print("Adeus")
        sair = False
    
    else:
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        if operacao == "+":
            soma = n1 + n2
            print(f"Soma de {n1:.2f} + {n2:.2f} = {soma:.2f}")
        
        elif operacao == "-":
            soma = n1 - n2
            print(f"Soma de {n1:.2f} - {n2:.2f} = {soma:.2f}")
        
        elif operacao == "*":
            soma = n1 * n2
            print(f"Soma de {n1:.2f} * {n2:.2f} = {soma:.2f}")
        
        elif operacao == "/":
            soma = n1 / n2
            print(f"Soma de {n1:.2f} / {n2:.2f} = {soma:.2f}")
    
        else:
            print("Operação inválida, tente novamente.")