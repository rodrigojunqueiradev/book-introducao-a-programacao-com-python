"""
28. Escreva um programa que solicite a velocalidade de um usuário.
Caso a velocidade ultrapasse 120 km/h, informe que o usuário foi multado e que o valor da múlta é: R$ 150 + R$50 por km acima de 120 km/h.
"""

print("Controle de Multas Ligeirinho")
velocidade = float(input("Informe sua velocidade em km/h: "))

velocidade_excedida = velocidade - 120
multa = 150 + (50 * velocidade_excedida)

if velocidade <= 120:
    print("Parabéns, você é um bom motorita")
elif velocidade > 120:
    print(f"Você está acima da velocidade, o valor da sua multa é R$ {multa:.2f}")