print('Exercício 10\n Criar um programa que leia quanto a pessoa tem na carteira e converta para Dolar')

d = int(input('Quanto você tem na carteira? '))
print('Com esse dinheiro você pode comprar US$ {:.2}'.format(d/3.27))
if d == 0:
    print('Só lagrimas!')