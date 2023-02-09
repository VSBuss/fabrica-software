'''Considere os cenários de problemas a serem resolvidos:
1- Um berçário deseja informatizar suas operações.

Quando um bebê nasce, algumas informações são armazenadas sobre ele, tais como:
nome, data do nascimento, peso do nascimento, altura, a mãe deste bebê e o médico que fez seu parto.

Para as mães, o berçário também deseja manter um controle, guardando informações como:
nome, endereço, telefone e data de nascimento. Para os médicos, é importante saber: CRM, nome, telefone celular e especialidade.

Para resolver o cenário 1 faça:
A) Levantamento de requisitos (funcionais e não funcionais);
B) Diagramas UML (Caso de Uso);
C) Documento com levantamento de requisitos e diagramas UML;
D) Algoritmo em python.
E) Apresentação da atividade (Em slides)
F) Ao finalizar a atividade coloque na pasta compartilhada no Microsoft Teams (crie uma pasta com a descrição “AtivAva1DevAlg” dentro de ambas as pastas dos membros da dupla).'''

recem_nascido = {
    'nome' : '',
    'data_nascimento' : '',
    'peso_nascimento' : 0,
    'altura' : 0,
    'mae_bebe' : '',
    'medico_parto' : '',
    }

mae  = {
    'nome' : '',
    'endereco' : '',
    'telefone' : 0,
    'data_nascimento' : ''   
}

medico = { 
    'nome' : '',
    'crm' : 0,
    'telefone' : 0,
    'especialidade' : ''
}

print('DIGITE OS DADOS DO RECÉM NASCIDO')
print(50 * '-')
recem_nascido['nome'] = str(input('Digite o nome do recém nascido: '))
recem_nascido['data_nascimento'] = str(input('Digite a data de nascimento: '))
recem_nascido['peso_nascimento'] = float(input('Digite o peso do nascimento em Kg: '))
recem_nascido['altura'] = int(input('Digite a altura do recém nascido em cm: '))
recem_nascido['mae_bebe'] = str(input('Digite o nome da mãe do recém nascido: '))
recem_nascido['medico'] = str(input('Digite o médico responsável pelo parto: '))

print(50 * '-')
print('DIGITE OS DADOS DA MÃE')
mae['nome'] = str(input('Digite o nome da mãe: '))
mae['endereco'] = str(input('Digite o endereço (RUA): '))
mae['telefone'] = (input('Digite o número de telefone: '))
mae['data_nascimento'] = str(input('Digite a data de nascimento da mãe: '))

print(50 * '-')
print('DIGITE OS DADOS DO MÉDICO')
medico['nome'] = str(input('Digite o nome do médico: '))
medico['crm'] = int(input('Digite o CRM do médico: '))
medico['telefone'] = int(input('Digite o número de telefone do médico: '))
medico['especialidade'] = str(input('Digite a especialidade do médico: '))

print(recem_nascido)
print(mae)
print(medico)