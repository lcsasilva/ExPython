
brasileirao = ('Palmeiras',
'Santos',
'Vasco da Gama', 'Grêmio', 'Rio Grande do Sul RS',
'Flamengo	Rio de Janeiro RJ',
'Corinthians',
'Internacional	Rio Grande do Sul RS',
'Cruzeiro	Minas Gerais MG',
'São Paulo	São Paulo SP',
'Atlético Mineiro	Minas Gerais MG',
'Botafogo	Rio de Janeiro RJ',
'Fluminense	Rio de Janeiro RJ',
'Coritiba	Paraná PR',
'Bahia	Bahia BA',
'Goiás	Goiás GO',
'Guarani	São Paulo SP',
'Sport	Pernambuco PE',
'Portuguesa	São Paulo ',
'Atlético Paranaense	Paraná PR',
'Vitória',)
print('-'*30)
print(f'Os cinco primeiros colocados da tabela do brasileirão são: {brasileirao[:5]}')
print('-'*30)
print(f'Os quatro últimos colocados na tabela são {brasileirao[-5:-1]}')
print('-'*30)
print(sorted(brasileirao))
print('-'*30)
colocado = brasileirao.index('Corinthians')
print(f'O Corinthians está na posição {colocado+1}')
print('-'*30)