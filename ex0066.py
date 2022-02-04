numero = contador = soma = 0
while True:
    numero = int(input('Digite um número\n'
                       'para parar digite[999]: '))
    if numero == 999:
        break
    contador += 1
    soma += numero
print(f'Foram digitados {contador} números e a soma dos números digitados é {soma}')