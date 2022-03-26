
frase = str(input('Escreva uma frase: ')).upper().strip()

print('Essa frase possui {} letras "a"'.format(frase.count('A')))
print('A primeira vez que a letra "a" aparece é na posição: ', frase.find('A')+1)
print('A ultima vez que a letra "a" aparece é na posição: ', frase.rfind('A')+1)
