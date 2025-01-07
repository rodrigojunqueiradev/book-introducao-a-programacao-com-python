"""
25. Faça um Programa que leia três números e mostre o maior, o menor e crie uma lista em ordem crescente deles.
"""

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

if n1 >= n2 and n1 >= n3:
    print(f"{n1} é o maior número")
    if n2 >= n3:
        print(f"{n3} é o menor número")
    else:
        print(f"{n3} é o menor número")
elif n2 >= n1 and n2 >= n3:
    print(f"{n2} é o maior número")
    if n1 >= n3:
        print(f"{n3} é o menor número")
    else:
        print(f"{n1} é o menor número")
else:
    print(f"{n3} é o maior número")
    if n1 >= n2:
        print(f"{n2} é o menor número")
    else: 
        print(f"{n1} é o menor número")

numeros = [n1, n2, n3]
print(f"A ordem crescente dos números é: {sorted(numeros)}")