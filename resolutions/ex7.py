"""
7. Crie uma lista com os números de 1 a 5 e:
Exiba em tela a lista;
Exiba em tela apenas o primeiro elemento;
Exiba em tela apenas o último elemento;
Exiba em tela o número 3;
Exiba em tela os dois primeiros elementos em formato de lista;
Exiba em tela o terceiro e o quanto elemento em formato de lista;
Adicione na posição inicial o elemento "some string";
Exiba em tela a lista;
Exiba na tela todos os elementos de uma só vez sem ser em formato de lista.
"""

# Crie uma lista com os números de 1 a 5:
example_list = list(range(1,6))

# Exiba em tela a lista:
print(example_list)

# Exiba em tela apenas o primeiro elemento:
print(example_list[0])

# Exiba em tela apenas o último elemento:
print(example_list[-1])

# Exiba em tela o número 3
print(example_list[2])

# Exiba em tela os dois primeiros elementos em formato de lista:
print(example_list[:2])

# Exiba em tela o terceiro e o quanto elemento em formato de lista:
print(example_list[2:4])

# Adicione na posição inicial o elemento "some string":
example_list[0] = "some string"

# Exiba em tela a lista:
print(example_list)

# Exiba na tela todos os elementos de uma só vez sem ser em formato de lista:
for counter in example_list:
    print(counter)