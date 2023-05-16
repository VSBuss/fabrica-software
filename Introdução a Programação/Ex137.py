import tkinter as tk

def concatenar_texto(texto):
    texto_atual = texto_caixa.get()
    texto_caixa.set(texto_atual + texto)

janela = tk.Tk()

texto_caixa = tk.StringVar()

caixa_texto = tk.Entry(janela, textvariable=texto_caixa)
caixa_texto.pack()

botao1 = tk.Button(janela, text="Botão 1", command=lambda: concatenar_texto("Botão 1"))
botao1.pack()

botao2 = tk.Button(janela, text="Botão 2", command=lambda: concatenar_texto("Botão 2"))
botao2.pack()

janela.mainloop()