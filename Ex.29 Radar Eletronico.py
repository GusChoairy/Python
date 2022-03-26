import random, math

velocidade = int(input('Informe a velocidade: '))

#CASO A VELOCIDADE SEJA RANDOMICA
#velocidade = random.randint(1, 140)

km_Ultrapassados = (velocidade-80)
multa = float(km_Ultrapassados*7)

print('A velocidade do carro foi de: {}km/h'.format(velocidade))

#SE A VELOCIDADE FOR MENOR OU IGUAL AO LIMITE:
if velocidade <= 80:
    print('Carro abaixo do limite de velocidade.')

#CASO ULTRAPASSE O LIMITE:
else:
    print('Você foi multado!')
    print('Limite ultrapassado em {}km/h.'.format(km_Ultrapassados))
    print('Valor da multa: R${:.2f}.'.format(multa))


