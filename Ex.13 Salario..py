print('EXERCÍCIO 13\n Fazer um algoritmo que mostre o salario e mostre seu novo salario com aumento de 15%')

s = float(input('Salario atual: R$ '))
a = float(s*15/100)
print('O novo salario com 15% de aumento é R${:.2f}'.format(s+a))