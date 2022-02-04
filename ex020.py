import random

aln_um = input('Digite o nome do primeiro aluno: ')
aln_dois = input('Digite o nome do segundo aluno: ')
aln_tres = input('Digite o nome do terceiro aluno: ')
als_quatro = input('Digite o nome do quarto aluno: ')

alunos = [aln_um, aln_dois, aln_tres, als_quatro]
random.shuffle(alunos)
print('A ordem de apresentação é {}.'.format(alunos))


