#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.​

import getpass

usuario = input("Informe o nome de usuário: ")
senha = getpass.getpass("Informe sua senha: ")

while usuario == senha:
    print("\nerro404")
    usuario = input("\nInforme o nome de usuário: ")
    senha = getpass.getpass("Informe sua senha: ")