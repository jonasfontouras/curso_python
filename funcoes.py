def calc_temp(c):
    '''
    A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit
    C é a temperatura em graus Celsius
    '''
    f = (9 * c + 160) / 5
    return f


help(calc_temp)

num = int(input('Graus em ºC:'))
print(calc_temp(num))


def calc_distancia(t, v):
    d = t * v
    return d


def calc_consumo_combustivel(c):
    '''
        a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.
        Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
        com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
        tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
    '''
    consumo = c / 12.0
    return consumo


t = float(input('Tempo: '))
v = int(input('Velocidade: '))
c = calc_distancia(t, v)

print(calc_distancia(t, v))
print(calc_consumo_combustivel(c))