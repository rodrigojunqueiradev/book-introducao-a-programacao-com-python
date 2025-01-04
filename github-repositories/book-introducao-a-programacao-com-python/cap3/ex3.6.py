materia1 = float(input("Informe a nota na matéria 1: "))
materia2 = float(input("Informe a nota na matéria 2: "))
materia3 = float(input("Informe a nota na matéria 3: "))

media = (materia1 + materia2 + materia3)/3

if media >= 7:
    print(f"Aprovado com média: {media:.2f}")
else:
    print(f"Reprovado com média: {media:.2f}")