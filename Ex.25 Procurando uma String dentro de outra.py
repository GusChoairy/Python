#nomeCompleto = str(input('Digite seu nome: '))
#nome = 'silva'
#nomeTitle = 'Silva'
#if nomeTitle in nomeCompleto or nome in nomeCompleto:
#   print('Seu nome possui ' +nomeTitle)
#else:
#   print('Seu nome nao possui ' +nomeTitle)

#MODO MELHORADO
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome possui Silva? {}'.format('silva' in nome.lower()))