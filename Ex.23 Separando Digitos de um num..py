#num = str(input('Digite um número de 0 a 9999: '))

#print('Unidade: {}\nDezena : {}\nCentena: {}\nMilhar : {}'.format(num[3], num[2],num[1],num[0]))

#CORRIGIDO
num = int(input('Digie um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}\nDezena : {}\nCentena: {}\nMilhar : {}'.format(u,d,c,m))