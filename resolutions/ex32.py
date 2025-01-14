"""
32. Crie um programa que solicite as notas durante um período letivo e a quantidade de provas realizadas e armazene essas notas em uma lista. Depois o programa deve calcular a média aritmética simples dessas notas
"""

notas = []
soma = 0
quantidade_provas = int(input("Quantas provas você teve? "))
x = 0

while x < quantidade_provas:
    nota = float(input(f"Nota {(x + 1)} = "))
    notas.append(nota)
    soma += nota
    x += 1

media = soma / quantidade_provas

print(f"Média final: {media:.2f}")
