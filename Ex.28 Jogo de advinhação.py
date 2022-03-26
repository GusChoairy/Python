import random
print('O VILAREJO DE KAHLINDOR ESTÁ EM CHAMAS, VOCÊ DEVE APOSTAR SUA ALMA CONTRA O DEMONIO MALTAEL PARA CONSEGUIR SALVAR SEUS AMIGOS E FAMÍLIA!!')
print('Tire um resultado no dado maior que o do Demônio para não perder sua alma e salvar seu vilarejo!')
print('O Temivel Demonio lança seus dados ao suspeito destino! O resultado não podia ser outro... ')
dadoD = int(random.randint(3,5))
dadoH = int(random.randint(0,4))
print('O dado do Demonio: ',(dadoD))
print('O seu dado:', (dadoH))
respostafinal = ('Parece que os Deuses sopraram pela sua sorte!! Da proxima vez garantirei que não estarão olhando por você!').upper()
if dadoH < dadoD:
    print('Ninguem nunca lhe ensinou a não apostar contra um Demônio!?RMRMRMRMhahaha...')
elif dadoD == dadoH:
    print('EMPATE!! Agora terá que advinhar o número que cairá no dado do Demõnio. Esperava que fosse ser assim tão facil?')
    advinhação = int(input('Agora Diga! Que numeros cairão nos dados? '))
    resposta = str(input('Tem CERTEZA da sua resposta? '))
    print(resposta)
    if resposta.lower().split() == 'sim':
        print('Pois bem! rmrmrmm...')
    else:
        print('Então será {} mesmo!'.format(advinhação))
        print('O Demonio lança seus dados e o resultado foi surpreendente!')
        print(dadoD,'e', dadoD)
        if dadoD == advinhação:
            print(respostafinal)
        else:
            print('O RESULTADO NÃO PODERIA SER OUTRO! SOMENTE UM ANIMAL PARA SER TÃO IGNORANTE A PONTO DE ACHAR QUE PODERIA GANHAR NUM JOGO DE AZAR O SENHOR DAS MARUAGEM!\nAGORA TODOS QUE CONHECE QUEIMARÃO E SUA ALMA ME SERVIRÁ PARA SEMPRE! Risus')
else:
    print(respostafinal)
