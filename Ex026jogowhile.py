from random import randint
numeropc = randint(0, 10)
contador = 0
print('''Ola, sou seu computador..
Acabei de pensar em um numero entre 0 e 10.
Sera que você consegue adivinhar? ''')
acertou = False
while not acertou:
    palpite = int(input('Qual é seu palpite: '))
    contador += 1
    if palpite == numeropc:
        acertou = True
    else:
        if palpite < numeropc:
            print('Mais..Tente mais uma vez')
        else:
            print('Menos..Tente mais uma vez')
print('Acertou em {} tentativas'.format(contador))
