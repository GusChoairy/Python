#EXERCICIO 17 FAZER UM PROGRAMA QUE LEIA O CATETO OPOSTO, CATETO ADJACENTE E ENCONTRE A HIPOTENUSA


import math

cat_Oposto = float(input('Informe o cateto oposto: '))
cat_Adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = math.hypot(cat_Adjacente, cat_Oposto)
#hipotenusa = sqrt(pow(cat_Oposto, 2) + pow(cat_Adjacente, 2))

print(' A hipotenusa é igual a {:.2f}'.format(hipotenusa))