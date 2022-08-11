sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in ('MFmf'):
    sexo = str(input('Opção inválida, digite seu sexo: ')).upper().strip()[0]
print('Seu sexo é {}'.format(sexo))