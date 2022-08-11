numero = int(input('Digite o numero para tabuada: '))
salto = int(input('Digite até que numero vai a tabuada: '))
for c in range(1, salto+1):
    total = numero * c
    print('{} x {} = {}'.format(c, numero, total))
