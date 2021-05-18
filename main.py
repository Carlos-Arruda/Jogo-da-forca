
from random import randint

palavras = ('gato', 'Carro')
opcao = randint(0,len(palavras))
jogo = palavras[opcao]

print('A sua palavra foi selecionada')

while True:    
    for c in jogo:
        print('-',end='')

    letra = str(input('Digite uma letra'))


print()
print(palavras[opcao])
