"""
26. Qual letra aparece mais vezes na frase abaixo? 
frase = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia cum nam deserunt fugit, repellat nihil voluptates rerum at tempore quisquam perferendis molestiae, a aperiam deleniti ea odio commodi natus sapiente.'
"""

frase = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia cum nam deserunt fugit, repellat nihil voluptates rerum at tempore quisquam perferendis molestiae, a aperiam deleniti ea odio commodi natus sapiente.'.lower()

i = 0

quantidade_de_letras = 0
letra_que_repetiu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantidade_de_letras_atual = frase.count(letra_atual)

    if quantidade_de_letras < quantidade_de_letras_atual:
        quantidade_de_letras = quantidade_de_letras_atual
        letra_que_repetiu_mais = letra_atual

    i += 1

print(f"A letra que apareceu mais vezes foi: {letra_que_repetiu_mais} {quantidade_de_letras} x")
    