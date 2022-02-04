frase = input('Digite uma frase qualquer: ').strip().lower()
print('A letra "A" aparece {} na frase.'.format(frase.count('a')+1))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(
    frase.rfind('a')
))
