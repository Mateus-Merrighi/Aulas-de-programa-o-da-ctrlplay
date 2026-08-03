import random

def saudacoes_GUI(nome):
    frases=["Eae fi bão, meu nome é " + nome +". Como posso te ajudar?", "Fala comigo meu rei", "Seja bem vindo ao "+ nome+"."]
    return frases[random.randint(0,2)]
def salva_sugestao(sugestao):
    with open ("BaseDeConecimento.txt", "a+")as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")

def buscaResposta_GUI(texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu= conhecimento.readline()
            
            if viu != "":
                    if jaccard(texto,viu)> 0.8:
                        proximalinha = conhecimento.readline()
                        if "Chatbot: " in proximalinha:
                            return proximalinha
        
            else:
                conhecimento.write("\n" + texto)
                return "Uau fiquei sem palvras para isso"
def exiberesposta_GUI(texto,resposta,nome):
   return resposta.replace("Chatbot", nome)
def jaccard(textoUsuario, textoBase):
    textoUsuario= limpa_frase(textoUsuario)
    textoBase= limpa_frase(textoBase)
    if len(textoBase)< 1: return 0
    else:
        palavras_em_comum=0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/ (len(textoBase.split()))
def limpa_frase(frase):
    tirar= ["?","!","...",".","Robson","\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase= frase.upper()
    return frase
    
