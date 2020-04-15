from tkinter import *
from os import listdir
import os
import random
from datetime import *
janelaPrincipal = Tk()
janelaPrincipal.geometry("500x600+150+50")
data_atual = date.today()
data_alterada = "{},{},{}".format(data_atual.day, data_atual.month, data_atual.year)
def ChecarVencimento():
    arquivoS = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivoS) == 0:
        print("Não há arquivos")
        return
    lista_dif = []
    for i in range(len(arquivoS)):
        arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], "r")
        arquivo = arquivo.readlines()
        for j in range(len(arquivo)):
            arquivo[j] = arquivo[j].replace('\n', '')
            arquivo[j] = arquivo[j].replace(" ", "")
        listaint = []
        for j in range(len(arquivo)):
            listaint.append(int(arquivo[j]))
        arquivo = listaint[1:]
        data = date(arquivo[2], arquivo[1], arquivo[0])
        lista_dif.append((data_atual - data).days)
    listaint = []
    for i in range(len(lista_dif)):
        listaint.append(int(lista_dif[i]))
    listavencida = []
    for i in range(len(lista_dif)):
        if lista_dif[i] > 0:
            listavencida.append(i)
    if len(listavencida) > 0:
        Conta = Tk()
        Conta.geometry("400x50+700+150")
        for i in range(len(listavencida)):
            Texto = Label(Conta, text= arquivoS[listavencida[i]] + " expirou e não está disponível para pagamento!")
            Texto.pack()
            os.remove("C:/Users/jab/Documents/Testes/" + arquivoS[listavencida[i]])
def btCadastro_click():
    Cadastro = Tk()
    Cadastro.geometry("400x300+200+200")
    TxtNome = Entry(Cadastro)
    TxtNome.place(x=140, y=50)
    TxtValor = Entry(Cadastro)
    TxtValor.place(x=140, y=110)
    TxtVencimento1 = Entry(Cadastro)
    TxtVencimento1.place(width=35, x=135, y=180)
    TxtVencimento2 = Entry(Cadastro)
    TxtVencimento2.place(width=35, x=185, y=180)
    TxtVencimento3 = Entry(Cadastro)
    TxtVencimento3.place(width=35, x=235, y=180)
    LblNome = Label(Cadastro, text='Nome da conta')
    LblNome.place(x=150, y=25)
    LblValor = Label(Cadastro, text='Valor')
    LblValor.place(x=180, y=85)
    LblVencimento = Label(Cadastro, text='Data de Vencimento')
    LblVencimento.place(x=145, y=155)
    def btCadastrar_click():
        Entrada = True
        chk1 = TxtVencimento1.get().isnumeric()
        chk2 = TxtVencimento2.get().isnumeric()
        chk3 = TxtVencimento3.get().isnumeric()
        chk4 = TxtValor.get().isnumeric()
        if TxtNome.get() == "" or TxtVencimento1.get() == "" or TxtVencimento2.get() == "" or TxtVencimento3.get() == "" or TxtValor.get() == "":
            Entrada = False
        if chk4 == False or chk1 == False or chk2 == False or chk3 == False:
            Entrada = False
        if Entrada == True:
            Valor = int(TxtValor.get())
            Vencimento1 = int(TxtVencimento1.get())
            Vencimento2 = int(TxtVencimento2.get())
            Vencimento3 = int(TxtVencimento3.get())
            if Vencimento1 > 31 or Vencimento2 > 12:
                Entrada = False
            elif Vencimento1 == 0 or Vencimento2 == 0 or Vencimento3 == 0:
                Entrada = False
            elif Valor == 0:
                print("Digite um valor maior que 0 para a conta!")
            else:
                arquivo = open("C:/Users/jab/Documents/Testes/" + TxtNome.get(), "w")
                arquivo.write(TxtValor.get())
                arquivo.write("\n")
                arquivo.write(TxtVencimento1.get())
                arquivo.write("\n")
                arquivo.write(TxtVencimento2.get())
                arquivo.write("\n")
                arquivo.write(TxtVencimento3.get())
        if Entrada == False:
            print("Entrada inválida")
    def btCancelar_click():
        Cadastro.destroy()
    btCadastrar = Button(Cadastro, width=15, text="Cadastrar", command=btCadastrar_click)
    btCadastrar.place(x=230, y=230)
    btCancelar = Button(Cadastro, width=15, text="Cancelar", command=btCancelar_click)
    btCancelar.place(x=70, y=230)
    Cadastro.resizable(width=False, height=False)
def btContas_click():
    arquivos = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivos) == 0:
        print("Não há arquivos")
        return
    for i in range(len(arquivos)):
        Conta = Tk()
        Conta.geometry("400x300+700+150")
        arquivo = open("C:/Users/jab/Documents/Testes/" + arquivos[i], 'r')
        Nome = arquivos[i]
        arquivo = arquivo.readlines()
        for j in range(len(arquivo)):
            arquivo[j] = arquivo[j].replace('\n', '')
            arquivo[j] = arquivo[j].replace(" ", "")
        Valor = arquivo[0]
        Vencimento1 = arquivo[1]
        Vencimento2 = arquivo[2]
        Vencimento3 = arquivo[3]
        LblNome = Label(Conta, text='Nome da conta')
        LblNome.place(x=150, y=25)
        LblValor = Label(Conta, text='Valor')
        LblValor.place(x=180, y=85)
        LblVencimento = Label(Conta, text='Data de Vencimento')
        LblVencimento.place(x=145, y=155)
        TxtNome = Label(Conta, text=Nome)
        TxtNome.place(x=180, y=50)
        TxtValor = Label(Conta, text=Valor)
        TxtValor.place(x=180, y=110)
        TxtVencimento1 = Label(Conta, text=Vencimento1 + "/")
        TxtVencimento1.place(width=35, x=160, y=180)
        TxtVencimento2 = Label(Conta, text=Vencimento2 + "/")
        TxtVencimento2.place(width=35, x=185, y=180)
        TxtVencimento3 = Label(Conta, text=Vencimento3)
        TxtVencimento3.place(width=35, x=210, y=180)
        Conta.resizable(width=False, height=False)
def btUrgencia_click():
    arquivoS = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivoS) == 0:
        print("Não há arquivos")
        return
    lista_dif = []
    for i in range(len(arquivoS)):
      arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], "r")
      arquivo = arquivo.readlines()
      for j in range(len(arquivo)):
          arquivo[j] = arquivo[j].replace('\n', '')
          arquivo[j] = arquivo[j].replace(" ", "")
      listaint = []
      for j in range(len(arquivo)):
          listaint.append(int(arquivo[j]))
      arquivo = listaint[1:]
      data = date(arquivo[2], arquivo[1], arquivo[0])
      lista_dif.append((data_atual - data).days)
    listaint = []
    for i in range(len(lista_dif)):
        listaint.append(int(lista_dif[i]))
    proximo = 0
    proximo_indice = 0
    for i in range(len(lista_dif)):
        if lista_dif[i] <= 0:
            proximo = lista_dif[i]
            proximo_indice = i
            break
    for i in range(len(lista_dif)):
        if lista_dif[i] <= 0:
            if lista_dif[i] > proximo:
                proximo = lista_dif[i]
                proximo_indice = i
    Conta = Tk()
    Conta.geometry("400x300+700+150")
    arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[proximo_indice], "r")
    Nome = arquivoS[proximo_indice]
    arquivo = arquivo.readlines()
    for j in range(len(arquivo)):
        arquivo[j] = arquivo[j].replace('\n', '')
        arquivo[j] = arquivo[j].replace(" ", "")
    Valor = arquivo[0]
    Vencimento1 = arquivo[1]
    Vencimento2 = arquivo[2]
    Vencimento3 = arquivo[3]
    LblNome = Label(Conta, text='Nome da conta')
    LblNome.place(x=150, y=25)
    LblValor = Label(Conta, text='Valor')
    LblValor.place(x=180, y=85)
    LblVencimento = Label(Conta, text='Data de Vencimento')
    LblVencimento.place(x=145, y=155)
    TxtNome = Label(Conta, text=Nome)
    TxtNome.place(x=180, y=50)
    TxtValor = Label(Conta, text=Valor)
    TxtValor.place(x=180, y=110)
    TxtVencimento1 = Label(Conta, text=Vencimento1 + "/")
    TxtVencimento1.place(width=35, x=160, y=180)
    TxtVencimento2 = Label(Conta, text=Vencimento2 + "/")
    TxtVencimento2.place(width=35, x=185, y=180)
    TxtVencimento3 = Label(Conta, text=Vencimento3)
    TxtVencimento3.place(width=35, x=210, y=180)
    Conta.resizable(width=False, height=False)
def btContaBarata_click():
    arquivoS = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivoS) == 0:
        print("Não há arquivos")
        return
    listadif = []
    for i in range(len(arquivoS)):
        arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], "r")
        arquivo = arquivo.readlines()
        for j in range(len(arquivo)):
            arquivo[j] = arquivo[j].replace('\n', '')
            arquivo[j] = arquivo[j].replace(" ", "")
        listaint = []
        for j in range(len(arquivo)):
            listaint.append(int(arquivo[j]))
        listadif.append(listaint[0:1])
    menor = listadif[0]
    indice = 0
    for i in range(len(listadif)):
        if listadif[i] < menor:
            menor = listadif[i]
            indice = i
    Conta = Tk()
    Conta.geometry("400x300+700+150")
    arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[indice], "r")
    Nome = arquivoS[indice]
    arquivo = arquivo.readlines()
    for j in range(len(arquivo)):
        arquivo[j] = arquivo[j].replace('\n', '')
        arquivo[j] = arquivo[j].replace(" ", "")
    Valor = arquivo[0]
    Vencimento1 = arquivo[1]
    Vencimento2 = arquivo[2]
    Vencimento3 = arquivo[3]
    LblNome = Label(Conta, text='Nome da conta')
    LblNome.place(x=150, y=25)
    LblValor = Label(Conta, text='Valor')
    LblValor.place(x=180, y=85)
    LblVencimento = Label(Conta, text='Data de Vencimento')
    LblVencimento.place(x=145, y=155)
    TxtNome = Label(Conta, text=Nome)
    TxtNome.place(x=180, y=50)
    TxtValor = Label(Conta, text=Valor)
    TxtValor.place(x=180, y=110)
    TxtVencimento1 = Label(Conta, text=Vencimento1 + "/")
    TxtVencimento1.place(width=35, x=160, y=180)
    TxtVencimento2 = Label(Conta, text=Vencimento2 + "/")
    TxtVencimento2.place(width=35, x=185, y=180)
    TxtVencimento3 = Label(Conta, text=Vencimento3)
    TxtVencimento3.place(width=35, x=210, y=180)
    Conta.resizable(width=False, height=False)
def btContaCara_click():
    arquivoS = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivoS) == 0:
        print("Não há arquivos")
        return
    listadif = []
    for i in range(len(arquivoS)):
        arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], "r")
        arquivo = arquivo.readlines()
        for j in range(len(arquivo)):
            arquivo[j] = arquivo[j].replace('\n', '')
            arquivo[j] = arquivo[j].replace(" ", "")
        listaint = []
        for j in range(len(arquivo)):
            listaint.append(int(arquivo[j]))
        listadif.append(listaint[0:1])
    maior = listadif[0]
    indice = 0
    for i in range(len(listadif)):
        if listadif[i] > maior:
            maior = listadif[i]
            indice = i
    Conta = Tk()
    Conta.geometry("400x300+700+150")
    arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[indice], "r")
    Nome = arquivoS[indice]
    arquivo = arquivo.readlines()
    for j in range(len(arquivo)):
        arquivo[j] = arquivo[j].replace('\n', '')
        arquivo[j] = arquivo[j].replace(" ", "")
    Valor = arquivo[0]
    Vencimento1 = arquivo[1]
    Vencimento2 = arquivo[2]
    Vencimento3 = arquivo[3]
    LblNome = Label(Conta, text='Nome da conta')
    LblNome.place(x=150, y=25)
    LblValor = Label(Conta, text='Valor')
    LblValor.place(x=180, y=85)
    LblVencimento = Label(Conta, text='Data de Vencimento')
    LblVencimento.place(x=145, y=155)
    TxtNome = Label(Conta, text=Nome)
    TxtNome.place(x=180, y=50)
    TxtValor = Label(Conta, text=Valor)
    TxtValor.place(x=180, y=110)
    TxtVencimento1 = Label(Conta, text=Vencimento1 + "/")
    TxtVencimento1.place(width=35, x=160, y=180)
    TxtVencimento2 = Label(Conta, text=Vencimento2 + "/")
    TxtVencimento2.place(width=35, x=185, y=180)
    TxtVencimento3 = Label(Conta, text=Vencimento3)
    TxtVencimento3.place(width=35, x=210, y=180)
    Conta.resizable(width=False, height=False)
def btPagar_click():
    def btDeletar_click():
        Nome = btConfirmar_click()
        arquivoS = listdir("C:/Users/jab/Documents/Testes")
        if len(arquivoS) == 0:
            print("Não há arquivos")
            return
        for i in range(len(arquivoS)):
            if Nome == arquivoS[i]:
                os.remove("C:/Users/jab/Documents/Testes/" + Nome)
                Conta = Tk()
                Conta.geometry("400x100+700+150")
                Texto = Label(Conta, text= Nome + " foi paga com sucesso!")
                Texto.pack()
    def btConfirmar_click():
        NomeC = None
        if Pagar.get() == "":
            print("Entrada inválida")
        else:
            Nome = Pagar.get()
            arquivoS = listdir("C:/Users/jab/Documents/Testes")
            for i in range(len(arquivoS)):
                if Nome == arquivoS[i]:
                    btDeletar = Button(Conta, width=20, text="Pagar", command=btDeletar_click)
                    btDeletar.place(x=135, y=320)
                    NomeC = arquivoS[i]
                    arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], 'r')
                    Nome = arquivoS[i]
                    arquivo = arquivo.readlines()
                    for j in range(len(arquivo)):
                        arquivo[j] = arquivo[j].replace('\n', '')
                        arquivo[j] = arquivo[j].replace(" ", "")
                    Valor = arquivo[0]
                    Vencimento1 = arquivo[1]
                    Vencimento2 = arquivo[2]
                    Vencimento3 = arquivo[3]
                    LblNome = Label(Conta, text='Nome da conta')
                    LblNome.place(x=155, y=125)
                    LblValor = Label(Conta, text='Valor')
                    LblValor.place(x=180, y=185)
                    LblVencimento = Label(Conta, text='Data de Vencimento')
                    LblVencimento.place(x=145, y=245)
                    TxtNome = Label(Conta, text=Nome)
                    TxtNome.place(x=180, y=150)
                    TxtValor = Label(Conta, text=Valor)
                    TxtValor.place(x=180, y=210)
                    TxtVencimento1 = Label(Conta, text=Vencimento1 + "/")
                    TxtVencimento1.place(width=35, x=155, y=270)
                    TxtVencimento2 = Label(Conta, text=Vencimento2 + "/")
                    TxtVencimento2.place(width=35, x=180, y=270)
                    TxtVencimento3 = Label(Conta, text=Vencimento3)
                    TxtVencimento3.place(width=35, x=205, y=270)
        return NomeC
    Conta = Tk()
    Conta.geometry("400x450+700+150")
    Pagar = Entry(Conta)
    Pagar.place(width=140,x=140,y=50)
    btConfirmar = Button(Conta, width=20, text="Buscar", command=btConfirmar_click)
    btConfirmar.place(x=135, y=80)
    Conta.resizable(width=False, height=False)
def btTotal_click():
    arquivoS = listdir("C:/Users/jab/Documents/Testes")
    if len(arquivoS) == 0:
        print("Não há arquivos")
        return
    listaint = []
    for i in range(len(arquivoS)):
        arquivo = open("C:/Users/jab/Documents/Testes/" + arquivoS[i], "r")
        arquivo = arquivo.readlines()
        print(arquivo)
        for j in range(len(arquivo)):
            arquivo[j] = arquivo[j].replace('\n', '')
            arquivo[j] = arquivo[j].replace(" ", "")
        listaint.append(int(arquivo[0]))
    total = sum(listaint)
    Conta = Tk()
    Conta.geometry("400x50+700+150")
    Texto = Label(Conta, text="O valor total que deve ser pago é de "+ str(total))
    Texto.pack()
def btSair_click():
    janelaPrincipal.destroy()
def btAtualizar_click():
    ChecarVencimento()
TxtData = Label(janelaPrincipal, text= "Data Atual")
TxtData.place(x=215, y=40)
LblData = Label(janelaPrincipal, text="|"+data_alterada+"|")
LblData.place(x=215, y=60)
btCadastro = Button(janelaPrincipal, width=20, text="Cadastrar Conta", command=btCadastro_click)
btCadastro.place(x=170, y=100)
btContas = Button(janelaPrincipal, width=20, text="Todas as Contas", command=btContas_click)
btContas.place(x=170, y=155)
btUrgencia = Button(janelaPrincipal, width=20, text="Vencimento Próximo", command=btUrgencia_click)
btUrgencia.place(x=170, y=210)
btContaBarata = Button(janelaPrincipal, width=20, text="Conta Mais Barata", command=btContaBarata_click)
btContaBarata.place(x=170, y=270)
btContaCara = Button(janelaPrincipal, width=20, text="Conta Mais Cara", command=btContaCara_click)
btContaCara.place(x=170, y=330)
btPagar = Button(janelaPrincipal, width=20, text="Pagar Conta", command=btPagar_click)
btPagar.place(x=170, y=390)
btTotal = Button(janelaPrincipal, width=20, text="Total a Pagar", command=btTotal_click)
btTotal.place(x=170, y=450)
btSair = Button(janelaPrincipal, width=20, text="Sair", command=btSair_click)
btSair.place(x=170, y=510)
btAtualizar = Button(janelaPrincipal, width=15, text="Atualizar", command=btAtualizar_click)
btAtualizar.place(x=185, y=5)
ChecarVencimento()
janelaPrincipal.resizable(width=False, height=False)
janelaPrincipal.mainloop()