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
root.title("Programa de Python Simples")




#Modificações feitas por mim
import random
senhacofre = [random.randint(1,5), random.randint(1,5), random.randint(1,5)]
jogador = [0,0,0]
acerto = 0
num = ''

def tentativa():
    if senhacofre == jogador:
        True
    else:
        False

def modificar_senha():
    acerto = 0
    if senhacofre[0] == jogador[0]:
        acerto = acerto + 1
    elif senhacofre[1] == jogador[1]:
        acerto = acerto + 1
    elif senhacofre[2] == jogador[2]:
        acerto = acerto + 1
    vertexto.set(acerto)

def senhajogador(num):
    a = num
    jogador[-1] = a
    vertexto.set(jogador)

def jogo():
    jogar = 0


#Plano de Fundo usando imagem
pic = PhotoImage(file=r"C:\Users\fabrica.aluno2\Pictures\Cofre.png")
label1 = Label(root, image=pic)
label1.place(x = -200, y = -20)



#Original
def limpar():
    numero1_entrada.delete(0, END)
    numero2_entrada.delete(0, END)

def soma():
    n1 = numero1.get()
    n2 = numero2.get()
    res = n1+n2
    vresultado.set(res)

def sub():
    n1 = numero1.get()
    n2 = numero2.get()
    res = n1-n2
    vresultado.set(res)

def mulp():
    n1 = numero1.get()
    n2 = numero2.get()
    res = n1*n2
    vresultado.set(res)

def divisao():
    n1 = numero1.get()
    n2 = numero2.get()
    res = n1/n2
    resarr = round(res,2)
    vresultado.set(resarr)

numero1 = DoubleVar()
numero2 = DoubleVar()
vnumero1 = Label(text="Número 1:",bg="#c3e8de",fg="black",font=("Arial","14","bold"))
vnumero1.place(relx=0.05,rely=0.3)
numero1_entrada= Entry(textvariable=numero1,font=("Arial","12","bold"),bg="white",fg="red",justify='center')
numero1_entrada.place(relx=0.2,rely=0.3,relwidth=0.1)

vnumero2 = Label(text="Número 2:",bg="#c3e8de",fg="black",font=("Arial","14","bold"))
vnumero2.place(relx=0.32,rely=0.3)
numero2_entrada= Entry(textvariable=numero2,font=("Arial","12","bold"),bg="white",fg="red",justify='center')
numero2_entrada.place(relx=0.48,rely=0.3,relwidth=0.1)

butlimpar = Button( text="Limpar", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'), command=limpar)
butlimpar.place(relx=0.05, rely=0.4, relwidth=0.15, relheight=0.15)
butsoma = Button( text="+", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=soma)
butsoma.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.15)
butsub = Button( text="-", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=sub)
butsub.place(relx=0.6, rely=0.4, relwidth=0.1, relheight=0.15)
butmult = Button( text="*", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=mulp)
butmult.place(relx=0.72, rely=0.4, relwidth=0.1, relheight=0.15)
butdiv = Button( text="/", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=divisao)
butdiv.place(relx=0.85, rely=0.4, relwidth=0.1, relheight=0.15)

texto1 = Label(text="Resultado:",bg="#c3e8de",fg="black",font=("Arial","14","bold"))
texto1.place(relx=0.6,rely=0.3)

vresultado = StringVar()
resultado=Label( textvariable=vresultado,bg="#FFFFFF",
                 font=('verdana', 14, 'bold'))
resultado.place(relx=0.75,rely=0.3,relwidth=0.2)





#Modificações feitas por mim

botaoteste = Button( text="Teste", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'),command=modificar_senha)
botaoteste.place(relx=0.05, rely=0.8, relwidth=0.09, relheight=0.1)

tituloJogo = Label(text="Jogo do Cofre:",bg="#6D6E71",fg="white",font=("Arial","20","bold"))
tituloJogo.place(x=300,y=22)

texto2 = Label(text="Números Certos:",bg="#c3e8de",fg="black",font=("Arial","14","bold"))
texto2.place(relx=0.2,rely=0.8, relheight=0.1)

vertexto = StringVar()
testeresultado=Label( textvariable=vertexto,bg="#FFFFFF",
                 font=('verdana', 14, 'bold'))
testeresultado.place(relx=0.45,rely=0.8,relwidth=0.2, relheight=0.1)


'''Botões numéricos do Cofre'''

buttomOne = Button( text="1", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=senhajogador(3))
buttomOne.place(x=400, y=300, relwidth=0.05, relheight=0.05)

buttomTwo = Button( text="2", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomTwo.place(x=450, y=300, relwidth=0.05, relheight=0.05)

buttomThree = Button( text="3", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomThree.place(x=500, y=300, relwidth=0.05, relheight=0.05)

buttomFour = Button( text="4", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomFour.place(x=400, y=350, relwidth=0.05, relheight=0.05)

buttomFive = Button( text="5", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomFive.place(x=450, y=350, relwidth=0.05, relheight=0.05)

buttomSix = Button( text="6", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomSix.place(x=500, y=350, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="7", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomSeven.place(x=400, y=400, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="8", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomSeven.place(x=450, y=400, relwidth=0.05, relheight=0.05)

buttomSeven = Button( text="9", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'))
buttomSeven.place(x=500, y=400, relwidth=0.05, relheight=0.05)




root.mainloop()