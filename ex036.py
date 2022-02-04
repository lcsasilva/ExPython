v_casa = float(input('Qual o valor da casa?: '))
v_salario = float(input('Qual o seu salário?: '))
financiamento = int(input('Em quantos anos será irá pagar?: '))
prestacao = v_casa/(financiamento*12)
limite_parcela = v_salario * 0.3

if limite_parcela < prestacao:
    print(f'Não será possível realizarmso esse emprestimo no momento,'
          f'pois a parcela de {prestacao:.2f} excede 30% do seu sálario.')
else:
    v_casa = v_casa/financiamento
    print('Seu emprestimo de R${:.2f} foi aprovado, em {}x de R${:.2f}'.format(
        v_casa, financiamento, prestacao
    ))