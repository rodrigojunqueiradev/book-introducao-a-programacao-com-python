"""
23. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido
"""

valor_hora = float(input("Informe o valor da sua hora: "))
horas = float(input("Informe quantas horas você trabalha por mês: "))

salario_bruto = valor_hora * horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("Folha de pagamento: ")
print(f"+ Salário Bruto: R$ {salario_bruto:.2f}")
print(f"- Desconto de Imposto de Renda: R$ {ir:.2f}")
print(f"- Desconto o INSS: R$ {inss:.2f}")
print(f"- Desconto do sindicato: R$ {sindicato:.2f}")
print(f"+ Salário Líquido: R$ {salario_liquido:.2f}")