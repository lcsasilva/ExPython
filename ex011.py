alt = int(input('Qual é a altura da parede?: '))
larg = int(input('Qual é a largura da parede?: '))

area = alt*larg

tn = area/2

print('Sua parede possuí {} metros quadrados,\n'
      'e será necessário {} litros de tinta para pintar.'
      .format(area, tn))
