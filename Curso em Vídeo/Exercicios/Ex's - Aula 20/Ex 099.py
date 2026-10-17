import time

def maior(*tupla):
    print(''+"-=" * 40)
    first = 0
    print('Os número apresentados foram: ', end="")
    for i in tupla:
        print(f'{i}..', end="", flush=True)
        time.sleep(0.4)
        if first == 0 or maior < i:
            maior = i
            first += 1
        else:
            pass
    
    print(f'\nO maior valor da lista encontrado foi: {maior}')
    print(f'Foram informados {len(tupla)} números ao todo')


maior(3, 5 ,8 ,7 ,9 ,1 , 8, 100, 2)
maior(0)
maior(1,3,2)