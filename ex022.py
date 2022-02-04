nome = input('Qual é o seu nome e sobrenome?: ')

print(nome.upper())
print(nome.lower())

espaco = nome.split()
juntar = "".join(espaco)
print(len(juntar))

pnome = espaco[0]
print(len(pnome))