from tkinter import *

def registra_vaga():

    pass

def visualisar_vagas():

    pass

def historico():

    pass

def iniciar_dia():

    pass

def main():

    janela = Tk()
    janela.title("Sistema de Gerenciamento de Estacionamento")

    botao1 = Button(janela, text="Registra vaga", command= registra_vaga)
    botao1.grid(column=0, row=0)

    botao2 = Button(janela, text="Visualisa vagas", command= visualisar_vagas)
    botao2.grid(column=1, row=0)

    botao3 = Button(janela, text="Historico", command= historico)
    botao3.grid(column=2, row=0)

    botao4 = Button(janela, text="Iniciar o dia", command= iniciar_dia)
    botao4.grid(column=3, row=0)

    texto = Label(janela, text="Bem vindo ao Sistema de Gerenciamento de Estacionamento",)
    texto.grid(column=1, row=1)

    janela.mainloop()
main()