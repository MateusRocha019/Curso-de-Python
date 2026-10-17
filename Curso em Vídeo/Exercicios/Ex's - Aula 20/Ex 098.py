import time

def contador(inicio, fim, passo):
    print("-=" * 44)

    if inicio <= fim:
        for i in range(inicio, fim+1, passo):
            print(f"{i}...", end="", flush=True)
            time.sleep(0.4)  
    else:
        for i in range(inicio, fim-1, (passo*(-1))):
            print(f"{i}...", end="", flush=True)
            time.sleep(0.4)
    print('\n'+"-=" * 44)


contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('Digite o número que deseja iniciar a contagem: '))
fim = int(input("Digite o último número da contagem: "))
passo = int(input('Digite de quantos em quantos número ele vai pular: '))
if passo < 0:
    passo = passo * -1
if passo == 0:
    passo = 1
contador(inicio, fim, passo)