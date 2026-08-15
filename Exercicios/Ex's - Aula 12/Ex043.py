print('Calculadora de IMC')

peso = float(input('Digite o seu pego em Kilos: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está com o peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')
