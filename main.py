from tkinter import *
import tkinter 


# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

janela=Tk()
janela.title("")
janela.geometry("400x200")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

#definindo variaveis globais

global tempo
global rodar
global contador
global limitador

limitador = 59
tempo= "00:00:00"
rodar= False
contador = -5

def iniciar():
    global tempo
    global contador
    global limitador
    
    if rodar:
        if contador <=-1:
            inicio = 'Comecando em ' + str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'

        else:
            label_tempo['font'] = 'Times 50 bold'
            
            temporario = str(tempo) 
            h,m,s= map(int, temporario.split(":"))
            h= int(h) 
            m= int(m) 
            s= int(contador)

            if (s>=limitador):
                contador = 0
                m+=1

            s= str(0)+str(s)
            m= str(0)+str(m)
            h= str(0)+str(h)

            temporario = str(h[-2:])+":" + str(m[-2:])+":" + str(s[-2:]) 
            label_tempo['text'] = temporario
            tempo = temporario





        label_tempo.after(1000, iniciar)
        contador +=1

def start():
    global rodar
    rodar = True
    iniciar()

def pausar():
    global rodar
    rodar = False
    
def reiniciar():
    global contador
    global tempo
    contador = 0 
    tempo = "00:00:00"
    label_tempo['text'] = tempo

#criando label
label_app = Label(janela, text='Cronômetro', font=(" Arial 10"), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=(" Times 50 bold"), bg=cor1, fg=cor3)
label_tempo.place(x=20, y=25)

#criando botões

botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy  13 bold'), relief= 'raised', overrelief='ridge')
botao_iniciar.place(x=20, y=130)

botao_pausar = Button(janela,command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy  13 bold'), relief= 'raised', overrelief='ridge')
botao_pausar .place(x=140, y=130)

botao_reiniciar = Button(janela,command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy  13 bold'), relief= 'raised', overrelief='ridge')
botao_reiniciar.place(x=260, y=130)

janela.mainloop()
 