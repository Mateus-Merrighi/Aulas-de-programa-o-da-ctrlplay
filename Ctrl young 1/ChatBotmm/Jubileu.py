import ProjetoChatBot as pc
from tkinter import *

main_window= Tk()
main_window.title("Jubileu")
main_window.geometry("500x700")

frame= Frame(main_window)
frame.grid()

l_indentif= Label(frame, text="Insira uma mensagem aqui: ")
l_indentif.grid(row=0,column=0)

e_mensagem = Entry(frame)
e_mensagem.grid( row=0, column=1)

frame2 = Frame(main_window)
frame2.grid(row= 1, column=0)
v= StringVar()
Label(frame2, textvariable=v, justify=LEFT).grid()

nome_maquina="Jubileu"
v.set("Qual seu nome?")
entrada_sugestao = False
entrada_nome_do_usuario = True
nome_usuario = ""
historico_conversa= ""

def roda_Chatbot():
    global entrada_sugestao
    global entrada_nome_do_usuario
    global nome_usuario
    global historico_conversa


    if entrada_nome_do_usuario:
        nome_usuario= e_mensagem.get()
        saudacao = pc.saudacoes_GUI(nome_maquina)
        historico_conversa = nome_maquina + ": " + saudacao + "\n"
        v.set(historico_conversa)
        entrada_nome_do_usuario= False
        e_mensagem.delete(0, END)
    else:
        texto= e_mensagem.get()
        historico_conversa += "\n" + nome_usuario + ": " + texto
        v.set(historico_conversa)
        e_mensagem.delete(0, END)

        if entrada_sugestao:
            pc.salva_sugestao(texto)
            entrada_sugestao =False
            historico_conversa += "\nAhhh agora eu entendi, agora eu saquei, agora as peças se encaixaram\n"
            v.set(historico_conversa)
        else:
            resposta = pc.buscaResposta_GUI("Robson: "+ texto+ "\n")

            if resposta == "Uau fiquei sem palvras para isso":
                historico_conversa += "\nPesquisa no google e me manda a resposta?\n"
                v.set(historico_conversa)
                entrada_sugestao = True
            else:
                historico_conversa += "\n" + pc.exiberesposta_GUI(texto, resposta, nome_maquina)
                v.set(historico_conversa)




Button(frame, text="Enviar", command=roda_Chatbot).grid(row=0, column=2)



main_window.mainloop()