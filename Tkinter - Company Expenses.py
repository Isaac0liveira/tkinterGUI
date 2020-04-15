from tkinter import *

def clicar():
    
      valor = in1.get()
      filtro = valor.isdigit()
      print(filtro)
      if(filtro == True):
          encargo_inss = float(valor) * 0.08
          encargo_fgts = float(valor)* 0.08
          encargo_ferias_decimo_seguros = float(valor) * 0.25
          encargos = float(encargo_inss) + float(encargo_fgts) + float(encargo_ferias_decimo_seguros)
          valor_final = float(valor) + float(encargos)
          aviso = "O gasto total da empresa com INSS, FGTS e outros encargos é " + str(valor_final)
          aviso2= "O encargo do INSS fica aproximadamente " + str(encargo_inss)
          aviso3 = "O encargo do FGTS fica aproximadamente " + str(encargo_fgts)
          lb ["text"] = aviso
          inss["text"] = aviso2
          fgts["text"] = aviso3
          if(float(valor) > 1693 and float(valor) <= 2822):
              encargo_inss = float(valor) * 0.09
              encargo_fgts = float(valor)* 0.08
              encargo_ferias_decimo_seguros = float(valor) * 0.25
              encargos = float(encargo_inss) + float(encargo_fgts) + float(encargo_ferias_decimo_seguros)
              valor_final = float(valor) + float(encargos)
              aviso = "O gasto total da empresa com INSS, FGTS e outros encargos é " + str(valor_final)
              aviso2= "O encargo do INSS fica aproximadamente " + str(encargo_inss)
              aviso3 = "O encargo do FGTS fica aproximadamente " + str(encargo_fgts)
              lb ["text"] = aviso
              inss["text"] = aviso2
              fgts["text"] = aviso3
          elif(float(valor) > 2822 and float(valor) <= 5645):
               encargo_inss = float(valor) * 0.11
               encargo_fgts = float(valor)* 0.08
               encargo_ferias_decimo_seguros = float(valor) * 0.23
               encargos = float(encargo_inss) + float(encargo_fgts) + float(encargo_ferias_decimo_seguros)
               valor_final = float(valor) + float(encargos)
               aviso = "O gasto total da empresa com INSS, FGTS e outros encargos é " + str(valor_final)
               aviso2= "O encargo do INSS fica aproximadamente " + str(encargo_inss)
               aviso3 = "O encargo do FGTS fica aproximadamente " + str(encargo_fgts)
               lb ["text"] = aviso
               inss["text"] = aviso2
               fgts["text"] = aviso3
          elif(float(valor) >= float(5645)):
               encargo_inss = 0 + float(621)
               aviso2= "O encargo do INSS fica aproximadamente " + str(encargo_inss)
               encargo_fgts = float(valor)* 0.08
               aviso3 = "O encargo do FGTS fica aproximadamente " + str(encargo_fgts)
               encargo_ferias_decimo_seguros = float(valor) * 0.25
               encargos = float(encargo_inss) + float(encargo_fgts) + float(encargo_ferias_decimo_seguros)
               valor_final = float(valor) + float(encargos)
               aviso = "O gasto total da empresa com INSS, FGTS e outros encargos é " + str(valor_final)
               
               lb ["text"] = aviso
               inss["text"] = aviso2
               fgts["text"] = aviso3
      else:
          lb["text"] = "Digite apenas números!"
          inss["text"] = "Digite apenas números!"
          fgts["text"] = "Digite apenas números!"
           
janela = Tk()
janela.title("Lucre ou Falhe")
janela["bg"] = "white"

in1 = (Entry(janela, font="arial 20 bold"))
in1.place(x = 90, y = 160)

lb2 = Label(janela, text= "Gastos da Empresa", font="arial 25 bold")
lb2.place(x = 90, y = 80)

lb = Label(janela, text= "")
lb.place(x = 80, y = 280)

inss = Label(janela, text= "")
inss.place(x = 80, y = 300)

fgts = Label(janela, text= "")
fgts.place(x = 80, y = 320)

bt = Button(janela, height = 2, width = 35, text="OK", command=clicar)
bt.place(x = 110, y = 220)
            
janela.geometry("500x500+100+150")
janela.mainloop()
