nome = input('Qual seu nome?: ').strip().lower()

sep = nome.split()
ult = len(sep)
print('Primeiro nome: {} \n'
      'Último nome: {}'.format(sep[0], sep[-1]))
