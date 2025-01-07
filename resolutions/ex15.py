"""
15. Crie uma lista de compras de supermercado com 8 itens e lista individualmente cada um dos itens dessa lista.
"""

lista = ['Chocolate', 'Leite', 'Pão', 'Café', 'Água', 'Carne', 'Arroz', 'Feijão']
cont = 1
for i in lista:
    print(f"{cont}. {i}")
    cont += 1