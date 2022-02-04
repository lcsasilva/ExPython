'''from time import sleep


print('-='*30)
for n in range(1, 11):
    sleep(0.5)
    print(n, end=' ')
print('FIM!')
print('-='*30)

for n in range(0, 11, -2):
    sleep(0.5)
    print(n, end=' ')
print('FIM!')
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('-='*30)
if passo == 0:
    passo = 1
if ini > fim:
    ini1 = ini
    fim1 = fim
    ini = fim1
    fim1 = ini1

def contador(i, f, p):
    for n in range(i, f, p):
        print(n, end=' ')
        sleep(0.5)
    print('FIM!')


contador(ini, fim, passo)'''
from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if p < 0:
        p *= -1
    if p == 0:
        p =1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end="")
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)