while True:
    print("-=" * 30)
    comando = input("Para sair do programa digite 'SAIR'\nDigite o nome do comando para mostrar as informações dele: ").strip().lower()

    if comando == "SAIR":
        break

    print("-=" * 30)
    help(comando)
    print("-=" * 30)
    
