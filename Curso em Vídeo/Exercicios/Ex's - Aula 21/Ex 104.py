def leiaInt():
    print("-=" * 30)
    while True:
        num_str = input("Digite um número: ")
        try:
            # Tenta converter a string recebida para inteiro
            num = int(num_str)
            break # Se a conversão der certo, quebra o loop
        except ValueError:
            # Se der erro (ex: usuário digitou 'abc' ou '5.5'), exibe a mensagem
            print("Você não digitou um número válido. Tente novamente.")
            print("-=" * 30)

    return num

num = leiaInt()
print(f"O número digitado foi: {num}")
print("-=" * 30)