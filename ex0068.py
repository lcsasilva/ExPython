from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
contador = 0

while True:
    maquina = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    opcao = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    resultado = (jogador + maquina) % 2
    if opcao == 'P' and resultado == 0:
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {maquina+jogador}, deu PAR!')
        print('Você GANHOU!!')
        contador += 1
    elif opcao == 'I' and resultado == 1:
        print('-'*30)
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {maquina+jogador}. deu ÍMPAR!')
        print('-'*30)
        print('Você GANHOU!!')
    elif opcao == 'P' and resultado == 1:
        print('-'*30)
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {maquina+jogador}. deu ÍMPAR!')
        print('-'*30)
        break
    elif opcao == 'I' and resultado == 0:
        print('-' * 30)
        print(f'Você jogou {jogador} e o computador {maquina}. Total de {maquina + jogador}. deu PAR!')
        print('-' * 30)
        break
print('Você perdeu!')
print(f'Você conquistou um total de {contador} vitórias consecutivas!')





