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


## Para usar o SQLITE você precisa baixar esse app: https://sqlitebrowser.org/dl/
## import sqlite3
import tkinter as tk

'''
## Criar conexão com o banco de dados
conexao = sqlite3.connect('jogo_do_cofre.db')
## Criar o cursor
cursor = conexao.cursor()
## Criar a tabela
cursor.execute("CREATE TABLE jogadores (nome text, data_atual text, recorde int)")
## Commit the changes
conexao.commit()
## Fechar a conexão com o BD
conexao.close()
'''


root = tk.Tk()
root.geometry("800x600")
root.resizable(0,0)
root.configure(bg="#002436")
## Título do programa
root.title("Jogo do Cofre")
limitador = 3
import random
import time

senhacofre = [random.randint(1,5), random.randint(1,5), random.randint(1,5)]
jogador = [0,0,0]
num = ''

'''
def cadastrar_recorde():

    ## Título dos Campos ou Labels
    label_nome = tkinter.Label(janela, text='Nome')
    label_nome.grid(row=0, column=0, padx=10, pady=10)
    
    label_data = tkinter.Label(janela, text='Data')
    label_data.grid(row=1, column=0, padx=10, pady=10)

    label_recorde = tkinter.Label(janela, text='Recorde')
    label_recorde.grid(row=2, column=0, padx=10, pady=10)

    ## Caixas de Entradas ou Inputs
    entry_nome = tkinter.Entry(janela, width=35)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)

    entry_data = tkinter.Entry(janela, width=35)
    entry_data.grid(row=1, column=1, padx=10, pady=10)

    entry_recorde = tkinter.Entry(janela, width=35)
    entry_recorde.grid(row=2, column=1, padx=10, pady=10)

    ## Limpa os dados das caixas de entrada
    entry_nome.delete(0, "end")
    entry_data.delete(0, "end")
    entry_recorde.delete(0, "end")

    ## Botão Cadastrar
    ##botao_salvar = tkinter.Button(text='SALVAR', command=)

    ## Realiza a conexão com o BD
    conexao = sqlite3.connect('jogo_do_cofre.db')
    cursor = conexao.cursor()
    ## Insere dados na tabela
    cursor.execute("INSERT INTO jogadores VALUES (:nome, :data_atual, :recorde)",
                   {
                       'nome': entry_nome.get(),
                       'data_atual': entry_data.get(),
                       'recorde': entry_recorde.get()
                   }
                   )
'''

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
        figura = tk.PhotoImage(file=r"")
        youwin = tk.Label(top, image=figura)
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
    
## Plano de Fundo usando imagem
pic = tk.PhotoImage(file=r"Introdução a Programação\Cofre.png")
bckground = tk.Label(root, image=pic)
bckground.place(x = -200, y = -20)

def btn1():
    jogar = 0

## Modificações feitas por mim
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = tk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = tk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        botaoteste = tk.Button( text="Teste", bd=2, bg='#107db2', fg='white',font=('verdana', 14, 'bold'), command=testar_senha)
        botaoteste.place(relx=0.05, rely=0.8, relwidth=0.09, relheight=0.1)

        tituloJogo = tk.Label(text="Jogo do Cofre:",bg="#6D6E71",fg="white",font=("Arial","20","bold"))
        tituloJogo.place(x=300,y=22)

        acertos = tk.Label(text="Acertos:",bg="#A7A9AC",fg="green",font=("Arial","10","bold"))
        acertos.place(x=420,y=250, relheight=0.05)

        texto_caixa = tk.StringVar()
        caixa_texto = tk.Label( textvariable=texto_caixa, bg='#FFFFFF', font=('verdana', 10, 'bold'))
        caixa_texto.place(x=400, y=200, relwidth=0.1, relheight=0.05)

        tentativateste = tk.StringVar()
        tentativa1 = tk.Label( textvariable=tentativateste, bg="#FFFFFF", fg='red', font=('verdana', 10, 'bold'))
        tentativa1.place(x=300, y=100, relwidth=0.1, relheight=0.05)



        qntacertos = tk.StringVar()
        testeresultado= tk.Label( textvariable=qntacertos,bg="#FFFFFF", font=('verdana', 10, 'bold'))
        testeresultado.place(x=475, y=252, relwidth=0.114, relheight=0.04)


        # BOTÕES NUMÉRICOS DO COFRE
        buttomOne = tk.Button( text="1", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('1'))
        buttomOne.pack()
        buttomOne.place(x=425, y=300, relwidth=0.05, relheight=0.05)

        buttomTwo = tk.Button( text="2", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('2'))
        buttomTwo.pack()
        buttomTwo.place(x=475, y=300, relwidth=0.05, relheight=0.05)

        buttomThree = tk.Button( text="3", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('3'))
        buttomThree.place(x=525, y=300, relwidth=0.05, relheight=0.05)

        buttomFour = tk.Button( text="4", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('4'))
        buttomFour.place(x=425, y=350, relwidth=0.05, relheight=0.05)

        buttomFive = tk.Button( text="5", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('5'))
        buttomFive.place(x=475, y=350, relwidth=0.05, relheight=0.05)

        buttomSix = tk.Button( text="6", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('6'))
        buttomSix.place(x=525, y=350, relwidth=0.05, relheight=0.05)

        buttomSeven = tk.Button( text="7", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('7'))
        buttomSeven.place(x=425, y=400, relwidth=0.05, relheight=0.05)

        buttomEight = tk.Button( text="8", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('8'))
        buttomEight.place(x=475, y=400, relwidth=0.05, relheight=0.05)

        buttomNine = tk.Button( text="9", bd=2, bg='#7ED63E', fg='black',font=('verdana', 8, 'bold'), command=lambda: altexto('9'))
        buttomNine.place(x=525, y=400, relwidth=0.05, relheight=0.05)

## Botão para sal
'''botao_recordes = Button(text='Recordes', command=cadastrar_recorde)'''

##Mantém a janela em aberto
root.mainloop()




############ https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/ ############