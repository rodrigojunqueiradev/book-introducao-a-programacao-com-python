"""
6. Peça para que o usuário digite um número, em seguida exiba em tela uma mensagem dizendo se tal número é PAR ou se é ÍMPAR.
"""

num = int(input("Número: "))

if (num % 2 ) == 0:
    print(f"{num} é PAR")
else:
    print(f"{num} é ÍMPAR")