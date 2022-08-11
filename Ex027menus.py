from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
sleep(0.3)
print('Analisando...')
sleep(0.5)
escolha = 0
while escolha != 5:
    print('''   Escolha as opções abaixo: 
    Digite [1] para SOMAR os valores digitados
    Digite [2] para MULTIPLICAR os valores digitados
    Digite [3] para saber o MAIOR numero digitado
    Digite [4] para escolher NOVOS numeros
    Digite [5] para SAIR do programa''')
    escolha = int(input('>>>>>>> Qual sua escolha? '))
    if escolha == 1:
        resultado = valor1 + valor2
        print('A soma dos valores é {} '.format(resultado))
    elif escolha == 2:
        resultado = valor1 * valor2
        print('A multiplicação dos valores é {} '.format(resultado))
    elif escolha == 3:
        if valor1 > valor2:
            print('O maior valor digitado é {}'.format(valor1))
        else:
            print('O maior valor digitado é {}'.format(valor2))
    elif escolha == 4:
        print('>>>> Informe o numeros novamente: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('FINALIZANDO!!! ')
    else:
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('FIM DO PROGRAMA, VOLTE SEMPRE!')




