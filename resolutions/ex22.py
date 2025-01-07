"""
22. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
Obs: C = 5 * ((F-32) / 9).
"""

graus_f = float(input("Informe a temperatura em graus Fahrenheit: "))

graus_c = 5  *((graus_f - 32) / 9)

print(f"A temperatura convertidade para Celsius é: {graus_c:.2f} °C")