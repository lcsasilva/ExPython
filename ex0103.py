'''def ficha(jogador, gol=0):
    if g
    print(f' O jogador {jogador} fez {gol}(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

ficha(nome, gols)
'''


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

#Programa Principal
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
