sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite seu sexo (F/M): ').strip().upper()[0]

    if sexo != 'F' and sexo != 'M':
        print('Você digitou errado algo errado tente novamente!\n')

if sexo == 'F':
    print(f'Seu sexo é feminino')
else:
    print('Seu sexo é masculino')
