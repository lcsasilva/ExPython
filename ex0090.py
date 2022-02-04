boletim = {}
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input('Média: '))
print(f'Nome é igual a {boletim["nome"]}')
print(f'Média é igual a {boletim["media"]}')
if boletim['media'] >= 7:
    boletim['situação'] = 'Aprovado'
else:
    boletim['situação'] = 'Reprovado'
print(f'A situação é {boletim["situação"]}')