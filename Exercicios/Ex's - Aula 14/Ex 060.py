num = int(input('Digite um número: '))
cont = num - 1
fat = num
print(num, end='')
while cont != 0:
    print(end=' x ')
    print(cont, end='')
    fat = fat * cont
    cont = cont - 1
print(f' = {fat}')
print(f'O valor fatorial de {num} é {fat}')
