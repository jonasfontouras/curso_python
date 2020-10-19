alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('notas.txt', 'w') as texto:
    for aluno, nota in alunos.items():
        texto.write(f'{aluno}, {nota}\n')

with open('notas.txt', 'r') as texto:
    for linha in texto:
        print(linha)