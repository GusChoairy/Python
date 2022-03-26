distancia_viagem = int(input('A distância da sua viagem é de quantos km: '))
tarifa1 = float(0.50 * distancia_viagem)
tarifa2 = float(0.45 * distancia_viagem)

if distancia_viagem <= 200:
    print('O valor da viagem é de R${:.2f}'.format(tarifa1))
else:
    print('O valor da viagem é de R${:.2f}'.format(tarifa2))
