print('-'*30)
print('LOJA DE SUPLEMENTOS DO DI')
print('-'*30)
contadorproduto = maisbaratopreco = soma = 0
continuar = ''
maisbaratonome = ''
while continuar != 'S':
    produto = str(input('Nome do Produto: ')).lower().strip()
    preco = int(input('Preço: R$ '))
    if continuar == 1:
        maisbaratopreco = preco
        maisbaratonome = produto
    elif preco < maisbaratopreco:
        maisbaratopreco = preco
        maisbaratonome = produto
    elif preco > 1000:
        contadorproduto += 1
    soma += preco
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
print('---------FIM DO PROGRAMA----------')
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {contadorproduto} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {maisbaratonome} que custa R${maisbaratopreco:.2f}')

