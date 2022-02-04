alunos = list()
nome = list()
notas = list()
dados = list()
while True:
    nome.append(str(input('Nome: ')))
    notas.append(int(input('Nota 1: ')))
    notas.append(int(input('Nota 2: ')))
    dados.append(nome[:])
    dados.append(notas[:])
    alunos.append(dados[:])
    nome.clear()
    notas.clear()
    dados.clear()
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
media = 0
aluno = list()
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for c in range(0, len(alunos)):
    aluno = alunos[c]
    media = sum(aluno[1])/2
    print(f'{alunos[c].index(aluno[0])}', end=' ')
    print(f'{aluno[0]:}', end=' ')
    print(f'{media:>8.1f}')
while True:
    na = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if na == "999":
        print('Finalizando...')
        break
    if na <= len(alunos) -1:
        print(f'Notas de {alunos[na][0]} são {alunos[na][1][0]} e {alunos[na][1][1]}')
print('Finalizando...')