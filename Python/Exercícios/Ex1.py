try:
    final_placa = int(input("Digite o último número da placa do seu veículo: "))
    dia = ''
    if final_placa == 1 or final_placa == 2:
        dia = "2ª Feira"
    elif final_placa == 3 or final_placa == 4:
        dia = "3ª Feira"
    elif final_placa == 5 or final_placa == 6:
        dia = "4ª Feira"
    elif final_placa == 7 or final_placa == 8:
        dia = "5ª Feira"
    elif final_placa == 9 or final_placa == 0:
        dia = "6ª Feira"
    else:
        print("Número da placa inválido")

    if final_placa < 0 or final_placa > 9:
        print("Entrada Inválida")
    else:
        print(f"Não é permitido circular com sua placa na {dia}.")

except ValueError:
    print("Entrada Inválida")