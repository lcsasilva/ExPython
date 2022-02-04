produto = float(input('Digite o valor do produto que gostaria de comprar:'))
pagamento = int(input('Digite o número correspondente com a forma de pagamento;\n'
                      '1 - À vista dinheiro\n'
                      '2 - À vista cartão\n'
                      '3 - em até 2x no cartão\n'
                      '4 - em até 3x no cartão\n'
                      ':'))
a_vista = produto*0.10
a_vista_cartao = produto*0.5
parcelado = produto*1.20

if pagamento != 1 or pagamento != 2 or pagamento != 3 or pagamento != 4:
    print('Escolha uma opção válida!')
elif pagamento == 1:
    print('Pagando à vista você ganhou 10% de desconto!\n'
          'Seu produto vai sair de R${:.2f} por R${:.2f}'.format(
        produto, a_vista
    ))
elif pagamento == 2:
    print('Pagando em 1x no cartão você ganha 5% de desconto!\n'
          'Seu produto vai sair de R${:.2f} por R${:.2f} '.format(
        produto, a_vista_cartao
    ))
elif pagamento == 3:
    print('Nessa forma de pagamento não haverá descontos!'
          'Seu produto irá sair por R${:.2f}'.format(
        produto
    ))
elif pagamento == 4:
    print('Parcelando em 3x no cartão, seu produto irá sair com'
          'um acréscima de 20%.\n'
          'de R${:.2} por R${:.2f}'.format(produto, parcelado))


