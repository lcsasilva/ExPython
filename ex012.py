prod = int(input('Qual é o preço do produto?: '))
desc = (prod/100)*95

print('O preço do produto é: {}$\n'
      'e com desconto de 5% ele vai sair por: {}$'
      .format(prod, desc))
