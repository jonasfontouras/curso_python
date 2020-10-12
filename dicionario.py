dic_notas = {"Jonas": 10, "Lucas": 7, "Matheus": 7}

soma = 0
for nome, notas in dic_notas.items():
    print(f'Aluno: {nome}, Nota: {notas}')

for notas in dic_notas.values():
    soma = soma + notas

media = soma / 3
print('Media total das notas: {}'.format(media))