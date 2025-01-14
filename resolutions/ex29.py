"""
29. Escreva um programa de aprovação de empréstimos.
O programa deve solicitar o valor do empréstimo, o salário da pessoa e a quantidade de anos a pagar.
O valor da prestação mensal não pode ser superior a 30% do salário.
O programa deve retornar se o empréstimo foi aprovado e o valor da prestação.
Obs: Não tem cobrança de juros.
"""

print("Sistema de empréstimos Juros Free")
valor_emprestimo = float(input("Informe o valor do empréstimo: R$ "))
salario = float(input("Informe o seu salário mensal: R$ "))
anos = int(input("Em quantos anos você deseja quitar a dívida? "))

meses = anos * 12
valor_mensal = valor_emprestimo / meses
validador = salario * 0.3

if valor_mensal <= validador:
    print(f"Empréstimo de R$ {valor_emprestimo:.2f} aprovado, você deve pagar {meses} parcelas de R$ {valor_mensal:.2f}.")
else:
    print(f"Empréstimo de R$ {valor_emprestimo:.2f} não aprovado, pois o valor mensal de R$ {valor_mensal:.2f} excede 30% do seu salário que é R$ {salario:.2f}")