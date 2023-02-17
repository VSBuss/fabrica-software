'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:

necessita da esfera;
necessita de limpeza; a. necessita troca do cabo ou conector; a. quebrado ou inutilizado Uma identificação igual a zero encerra o programa.

Ao final o programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%

'''

print("Tipos de defeitos a serem catalogados:\n"
"1- necessita da esfera\n"
"2- necessita de limpeza\n"
"3- necessita troca do cabo ou conector\n"
"4- quebrado ou inutilizado\n")

mouseids = []
um = dois = tres = qtro = 0

while True:
    ident = int(input("Mouse ID: "))
    if ident == 0:
        break
    defeito = int(input("Defeito: "))
    mouseids.append(ident)
    match defeito:
        case 1:
            um += 1
        case 2:
            dois += 1
        case 3:
            tres += 1
        case 4:
            qtro += 1
        case _:
            print("Valor inválido.")

print(f"\nQuantidade de mouses: {um+dois+tres+qtro}\n\n"
"Situação                        Quantidade              Percentual\n"
f"1- necessita da esfera                  {um}                     {um*100/(um+dois+tres+qtro):.2f}%\n"
f"2- necessita de limpeza                 {dois}                     {dois*100/(um+dois+tres+qtro):.2f}%\n"
f"3- necessita troca do cabo ou conector  {tres}                     {tres*100/(um+dois+tres+qtro):.2f}%\n"
f"4- quebrado ou inutilizado              {qtro}                     {qtro*100/(um+dois+tres+qtro):.2f}%\n")