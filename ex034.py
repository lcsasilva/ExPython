sal = int(input('Qual o seu salário?: '))
sup = 1250
if sal > sup:
    sal1 = sup*1.10
    print('Seu salário era R${:.2f},'
          'com aumento ficou R${:.2f}'.format(sal, sal1))
else:
    sal1 = sal*1.15
    print('Seu salário era R${:.2f},'
          'com aumento ficou R${:.2f}'.format(sal, sal1))