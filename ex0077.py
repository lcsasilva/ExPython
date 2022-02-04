palavras = ('aprender', 'programar', 'whey', 'academia', 'lolzin', 'estudar', 'meuovo')

for p in palavras:
        print(f'\nNa palavra {p} temos ', end=' ')
        for letra in p:
            if letra.lower() in 'aeiou':
                print(letra.upper(), end=' ')
