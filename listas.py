i = 0
lista = []
while i < 5:
    i = i + 1
    numero = int(input('Digite um número: ( {} )'.format(i)))
    lista.append(numero)
print(lista)

soma = 0
for num in lista:
    soma = soma + num

print('Soma: {}'.format(soma))