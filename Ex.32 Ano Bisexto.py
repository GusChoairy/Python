from datetime import date

ano = int(input('Digite um ano para saber se ele é bissexto: \nOu Digite 0 para escolher o ano atual!'))
if ano == 0:
    ano == date.today().year

if ano%100 != 0 and ano%4 == 0 or ano%400 == 0:
    print('O ano é bissexto!')
else:
   print('O ano não é bissexto!')