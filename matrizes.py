import numpy as np

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

soma = 0
print('Matriz:')
for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):

        soma = soma + matriz[i][j]

print('Soma dos números da matriz: {}'.format(soma))