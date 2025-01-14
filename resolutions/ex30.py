"""
30. Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.
Pergunte ao usuário a quantidade de kWh consumida e o tipo de estabelicimento (R para residências, I para indústrias e C para comércios).
Calcule o preço a pagar conforme a tabela:

Tipo | kWh           | Preço
R    | Até 500       | R$ 0,40
R    | Acima de 500  | R$ 0,65
C    | Até 1000      | R$ 0,55 
C    | Acima de 1000 | R$ 0,60
I    | Até 5000      | R$ 0,55
I    | Acima de 5000 | R$ 0,60

"""

print("Sistema de cobrança de energia elétrica")
consumo = float(input("Informe o consumo em kWh: "))
tipo_estabelecimento = input("Informe o tipo do estabelecimento, sendo: \nR para Resendências \nI para indústrias \nC para comércios \nTipo (R, I ou C): ")

if tipo_estabelecimento == "R" and consumo <= 500:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.4):.2f} ")
elif tipo_estabelecimento == "R" and consumo > 500:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.55):.2f} ")
elif tipo_estabelecimento == "C" and consumo <= 1000:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.55):.2f} ")
elif tipo_estabelecimento == "C" and consumo > 1000:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.55):.2f} ")
elif tipo_estabelecimento == "I" and consumo <= 5000:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.55):.2f} ")
elif tipo_estabelecimento == "I" and consumo > 5000:
    print(f"Tipo: {tipo_estabelecimento} \nConsumo: {consumo:.2f} \nValor a pagar: {(consumo*0.55):.2f} ")
else:
    print("Dados inválidos.")