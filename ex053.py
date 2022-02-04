palavra = input('Digite uma frase: ').strip().lower()

p_reverso = palavra[::-1]

print(palavra)
if p_reverso == palavra:
    print('Essa frase é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo!')