"""
24. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input("Informe uma letra: ").lower()
vogal = ['a', 'e', 'i', 'o', 'u']

if letra in vogal:
    print(f"A letra '{letra}' é uma vogal!")
else:
    print(f"A letra '{letra}' é uma consoante!")