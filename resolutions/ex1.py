"""
1. Crie um código que pergunte o salário de uma pessoa e faça a validação:
Se a pessoa ganhar mais de 1200 informe que ela deve pagar impostos.
"""

salario = float(input("Qual seu salário? "))

if salario >= 1200:
    print("Você deve pagar impostos!")
else:
    print("Você já ganha pouco demais para pagar impostos!")