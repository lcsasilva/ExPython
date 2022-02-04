def notas(n1=0, n2=0, n3=0, n4=0, sit=False):
    """
    :param n1, 2, 3 e 4: são as notas a serem somadas
    :param sit: Se deseja mostrar a situação do aluno sit=True
    :return: retorna soma das notas, média, maior  e menor nota
    """
    alunos = dict()
    lista = [n1, n2, n3, n4]
    soma = len(lista)
    media = n1 + n2 + n3 + n4 / 4
    menor = min(lista)
    maior = max(lista)
    alunos['total'] = soma
    alunos['maior'] = maior
    alunos['menor'] = menor
    alunos['media'] = media
    if sit == True:
        if 6 < media > 8:
            alunos['situação'] = 'BOA'
        elif media < 6:
            alunos['situação'] = 'RUIM'
        elif media > 8:
            alunos['situação'] = 'OTIMA'
    return alunos


#programa principal
alunos = dict()
resp = notas(7, 4, 10, 8, sit=False)
print(resp)