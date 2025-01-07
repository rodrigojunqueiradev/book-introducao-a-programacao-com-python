"""
9. Crie um programa que peça o nome, a idade, a altura e o peso de uma pessoa, depois calcule o IMC.
IMC = peso / altura ao quadrado
"""

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura: "))
peso = float(input("Peso: "))

imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, tem altura de {altura:.2f} metros, pesa {peso:.2f} e tem IMC no valor de {imc:.2f}")
