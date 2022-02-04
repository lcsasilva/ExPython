'''def maior(*num):
    print('Analisando os valores passados...')
    m = list(num)
    print(f'Os valores digitados foram {num}, um total de {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {num}.')
    print(max(m))


valores = list()

while True:
    n = int(input('Digite um valor: [999 para parar] '))
    if n == 999:
        break
    valores.append(n)

maior(valores) '''
from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

#programa principal
maior(2, 9, 4, 5,7, 1)
maior(2)
maior(2, 3, 6)
maior(4, 2)
maior(10, 8, 2, 8)