import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

list = [aluno4, aluno3, aluno2, aluno1]

escolhido = random.choice(list)

print('O aluno sorteado foi {}'.format(escolhido))