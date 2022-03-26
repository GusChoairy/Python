print('Exercício 11\n Fazer um programa que leia a largura e altura de uma parede em metros, calcule sua área e a quantidade de tinta necessaria para pinta-la (cada litro de tinta pinta 2m.)')

l= float(input('Largura da parede em metros:'))
a= float(input('Altura da parede em metros: '))
ar= a*l
print('A área da parede é de {:.2f}m e serão necessários {:.2f}L de tinta, para pintar a parede.'.format(ar,ar/2))
