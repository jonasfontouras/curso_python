import re

frase = 'Tenho 17 anos, meu cep é 96540-000. meu site é https://www.teste.com'

print(re.findall('\d{5}-\d{3}', frase))
print(re.findall('\d', frase))
print(re.findall('https?://[A-Za-z0-9./]+', frase))