
from math import sin, cos, tan, radians

angulo = float(input('Informe o angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tang= tan(radians(angulo))

print('O angulo possui SENO: {:.2f}\nO angulo possui COSSENO: {:.2f}\nO angulo possui e sua TANGENTE: {:.2f}'.format(sen, cos, tang))

