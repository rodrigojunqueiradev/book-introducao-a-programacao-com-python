"""
8. Crie um dicionário para as frutas e sua respectivas quantidades e depois faça o que se pede:
Apples, quantidade 5
Oranges, quantidade 8
Bananas, quantidade 13
a. Converta o dicionário em uma lista de frutas;
b. Adicione a essa lista a fruta 'pears';
c. Ordene a lista criada em ordem alfabética.
"""

# Crie um dicionário para as frutas e sua respectivas quantidades:
fruit_dict = {'apples':5, 'oranges':8, 'bananas':13}
print(fruit_dict)

# a. Converta o dicionário em uma lista de frutas:
fruit_list = list(fruit_dict)
print(fruit_list)

# b. Adicione a essa lista a fruta 'pears':
fruit_list = fruit_list + ['pears']
print(fruit_list)

# c. Ordene a lista criada em ordem alfabética:
print(sorted(fruit_list))