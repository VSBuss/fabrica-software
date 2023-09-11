x = 'S'
pontos_por_semestre = [0,0]
print("Programa de fidelidade LivrariaRia =)\n")
while x == 'S':
    datac = input("Informe a data da compra (dd/mm): ")
    if len(datac) == 5 and True == datac[0].isnumeric() and True == datac[1].isnumeric() and True == datac[3].isnumeric() and True == datac[4].isnumeric() and datac[2] == '/':
        mes = datac[3] + datac[4]
        mes = int(mes)
        dia = datac[0] + datac[1]
        dia = int(dia)
        if 0 < mes < 13 and 0 < dia < 32:
            while True:
                if mes<=6:
                    semestre = 0
                else:
                    semestre = 1
                qntlivros = input("Informe a quantidade de livros:")
                if True == qntlivros.isnumeric() and True == (int(qntlivros)>0):
                    qntlivros = int(qntlivros)
                    if qntlivros == 1:
                        pontos_por_semestre[semestre] += 5
                    elif qntlivros == 2:
                        pontos_por_semestre[semestre] += 15
                    elif qntlivros == 3:
                        pontos_por_semestre[semestre] += 30
                    elif qntlivros >= 4:
                        pontos_por_semestre[semestre] += 60
                    while True:
                        x = input("Deseja continuar cadastrando? (S/N)")
                        x = x.upper()
                        if x == 'S':
                            break
                        elif x == 'N':
                            print(f"\nSeu saldo atual é de {pontos_por_semestre[0]} pontos no primeiro semestre.\n"
                                  f"E de {pontos_por_semestre[1]} pontos no segundo semestre.\n")
                            exit()
                        else:
                            continue
                        break
                else:
                    print("Erro")
                    continue
                break
    else:
        print("Data Inválida.")
        continue