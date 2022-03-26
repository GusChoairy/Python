import random
from math import trunc, ceil, floor

num = random.uniform(0, 100)
#num = float(input('Digite um numero: '))

print('O numero {} tem a parte inteira {}, arredondando para cima temos {} e para baixo {}.'.format(num, trunc(num), ceil(num), floor(num) ))
