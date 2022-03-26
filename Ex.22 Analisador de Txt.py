nome = str(input('Digite aqui seu nome completo: ')).strip()

print('Nome em maiusculo: ',nome.upper())
print('Nome em minusculo: ',nome.lower())
#print('Quantas letras seu nome possui: ', len(nome.replace(" ", "")))
#print('Quantas letras possui seu primeiro nome: ', len((nome.split()[0])))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
