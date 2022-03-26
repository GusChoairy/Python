print('EXERCÍCIO 15\n Desenvolva um programa que pergunte a quantidade de km pecorrido por um carro alugado, a quantidade de dias que esteve alugado e que calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por KM rodado.')

d = int(input('Por quantos dias o carro foi alugado? '))
k = float(input('Quantos Km o carro andou? '))
vd = d * 60
vk = k * 0.15

print('O carro foi alugado por {} dias e andou {}Km, devendo ser pago um total de R${:.2f}'.format(d, k, vd+vk))