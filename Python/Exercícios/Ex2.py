try:
    print("    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    \n"
          "  ▓██■██■█╔════╗█■██■██▓  \n"
          "▓█■■██■■██╬Menu╬██■■██■■█▓\n"
          "╔╦╦╦╦╦╦╦╦╦╬╦╦╦╦╬╦╦╦╦╦╦╦╦╦╗\n"
          "║Bifão da massa ║ R$25,00║\n"
          "║Pankovo russo  ║ R$10,00║\n"
          "║Salada ladalada║ R$08,88║\n"
          "║Escargado      ║ R$19,99║\n"
          "║Pastel de sonho║ R$12,50║\n"
          "╚═══════════════╩════════╝\n")
    escolha = int(input("Digite o número do prato desejado: "))
    valor = 0
    while escolha <=0 or escolha > 5:
        print("Digita certo ae, lek.")
        escolha = int(input("Digite o número do prato desejado: "))
    match escolha:
        case 1:
            valor =+ 25
        case 2:
            valor =+ 10
        case 3:
            valor =+ 8.88
        case 4:
            valor =+ 19.99
        case 5:
            valor =+ 12.5

    gor_jetta = input("Aceita pagar a gorjeta do garçom 10% sobre o valor do prato? ")
    gor_jetta = gor_jetta.upper()
    if gor_jetta == 'S':
        print(f"Valor final: R${valor*1.1:.2f}")
    elif gor_jetta == 'N':
        print(f"Valor final: R${valor}")
    else:
        print("Entrada Inválida")

except ValueError:
    print("Entrada Inválida")