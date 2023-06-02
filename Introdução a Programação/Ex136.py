'''Neste exercício, você vai criar um jogo chamado Jogo do Cofre, onde 
o objetivo do jogador é acertar a senha de um cofre. A cada tentativa,
o jogo informará quantos números o jogador acertou e quantos números o jogador errou.

Crie uma classe com um método que recebe uma tentativa de senha como parâmetro
e retorna True se a tentativa estiver correta ou False caso contrário. A senha deve ser
uma lista de 3 números inteiros aleatórios entre 1 e 5.

Modifique o método verificar_senha para que, caso a tentativa esteja incorreta,
ele retorne uma mensagem informando quantos números o jogador acertou e quantos
números o jogador errou. Para isso, percorra os números da tentativa e compare
com os números da senha, verificando se eles estão na mesma posição. Se um número
estiver na mesma posição, ele é um acerto. Caso contrário, é um erro. Armazene os
acertos e erros em uma lista e imprima a mensagem informando quais números foram
acertados e quais foram errados.

Crie uma classe chamada Jogo com um método jogar que recebe uma instância da
classe Cofre como parâmetro e controla as tentativas do jogador. O jogador terá
n tentativas para acertar a senha. A cada tentativa incorreta, o jogo informará
quantas tentativas ainda restam.

Modifique o método jogar para que, caso a tentativa esteja incorreta, ele imprima
a mensagem informando quantos números o jogador acertou e quantos números o jogador
errou. Caso a tentativa esteja correta, ele deve imprimir uma mensagem informando que
a senha foi correta e encerrar o jogo.

Crie uma instância da classe Jogo e chame o método jogar para iniciar o jogo.'''

from tkinter import *
root = Tk()
root.geometry("800x600")
root.resizable(0,0)
root.configure(bg="#002436")
'''Título do programa'''
root.title("Programa de Python Simples")
limitador = 3
import random
import time

senhacofre = [random.randint(1,5), random.randint(1,5), random.randint(1,5)]
jogador = [0,0,0]
num = ''

def tentativa():
    if senhacofre == jogador:
        True
    else:
        False

def testar_senha():
    texto_teste = texto_caixa.get()
    jogador[0] = int(texto_teste[0])
    jogador[1] = int(texto_teste[1])
    jogador[2] = int(texto_teste[2])
    acerto = 0
    if senhacofre[0] == jogador[0]:
        acerto = acerto + 1
    if senhacofre[1] == jogador[1]:
        acerto = acerto + 1
    if senhacofre[2] == jogador[2]:
        acerto = acerto + 1
    qntacertos.set(acerto)
    tentativateste.set(texto_teste)
    if acerto == 3:
        time.sleep(3)
        top = Toplevel()
        top.title("VOCÊ GANHOU!")
        top.geometry("400x300")
        '''Foto caso vença'''
        figura = PhotoImage(file=r"")
        youwin = Label(top, image=figura)
        youwin.pack()



def senhajogador(num):
    a = num
    jogador[-1] = a
    qntacertos.set(jogador)

def jogo():
    jogar = 0

def altexto(numero):
    texto_atual = texto_caixa.get()
    if len(texto_atual) < 3:
        texto_caixa.set(texto_atual + numero)
    if len(texto_atual) == limitador:
        texto_caixa.set(texto_atual[1:3] + numero)
    else:
        texto_caixa.set(texto_atual + numero)
    
'''Plano de Fundo usando imagem'''
pic = PhotoImage(file=r"Introdução a Programação\Cofre.png")
bckground = Label(root, image=pic)
bckground.place(x = -200, y = -20)

def btn1():
    jogar = 0

'''Modificações feitas por mim'''

botaoteste = Button( text="Teste", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'), command=testar_senha)
botaoteste.place(relx=0.05, rely=0.8, relwidth=0.09, relheight=0.1)

tituloJogo = Label(text="Jogo do Cofre:",bg="#6D6E71",fg="white",font=("Arial","20","bold"))
tituloJogo.place(x=300,y=22)

acertos = Label(text="Acertos:",bg="#A7A9AC",fg="green",font=("Arial","10","bold"))
acertos.place(x=420,y=250, relheight=0.05)

texto_caixa = StringVar()
caixa_texto = Label( textvariable=texto_caixa, bg='#FFFFFF', font=('verdana', 10, 'bold'))
caixa_texto.place(x=400, y=200, relwidth=0.1, relheight=0.05)

tentativateste = StringVar()
tentativa1 = Label( textvariable=tentativateste, bg="#FFFFFF", fg='red', font=('verdana', 10, 'bold'))
tentativa1.place(x=300, y=100, relwidth=0.1, relheight=0.05)



qntacertos = StringVar()
testeresultado=Label( textvariable=qntacertos,bg="#FFFFFF", font=('verdana', 10, 'bold'))
testeresultado.place(x=475, y=252, relwidth=0.114, relheight=0.04)


'''Botões numéricos do Cofre'''

buttomOne = Button( text="1", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('1'))
buttomOne.pack()
buttomOne.place(x=425, y=300, relwidth=0.05, relheight=0.05)

buttomTwo = Button( text="2", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('2'))
buttomTwo.pack()
buttomTwo.place(x=475, y=300, relwidth=0.05, relheight=0.05)

buttomThree = Button( text="3", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('3'))
buttomThree.place(x=525, y=300, relwidth=0.05, relheight=0.05)

buttomFour = Button( text="4", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('4'))
buttomFour.place(x=425, y=350, relwidth=0.05, relheight=0.05)

buttomFive = Button( text="5", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('5'))
buttomFive.place(x=475, y=350, relwidth=0.05, relheight=0.05)

buttomSix = Button( text="6", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('6'))
buttomSix.place(x=525, y=350, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="7", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('7'))
buttomSeven.place(x=425, y=400, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="8", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('8'))
buttomSeven.place(x=475, y=400, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="9", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('9'))
buttomSeven.place(x=525, y=400, relwidth=0.05, relheight=0.05)




root.mainloop()