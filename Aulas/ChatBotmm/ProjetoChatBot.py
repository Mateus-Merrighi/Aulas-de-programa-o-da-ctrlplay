import random

def saudacoes(nome):
    frases=["Eae fi bão, meu nome é " + nome +". Como posso te ajudar", "Fala comigo meu rei", "Seja bem vinod ao "+ nome+"."]
    print(frases[random.randint(0,2)])
def recebaTexto():
    texto= "Robson: "+ input("Robson: ")

    palavraProibida= ["Filha de uma Fruta", "Catapimbas", "Vai para casa do tio patinhas", "Vai pra fruta que te pariu"]

    for p in palavraProibida:
        if p in texto:
            print("Vai cagar no mato, se mandar mais um palavriado chulo irei te banir do roblox")
            return recebaTexto()    
    return texto


def buscaResposta(nome,texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu= conhecimento.readline()
            
            if viu != "":
                if texto.replace("Robson: ", "")== "Tchau":
                    print(nome+ ": espero te ver denovo aqui! ")
                    return "fim"
                elif viu.strip()== texto.strip():
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                print("Se você não sabe imagina eu que nasci esse dias")
                conhecimento.write("\n" + texto)
                resposta_user = input("Pesquisa no google e me manda a resposta?\n")
                conhecimento.write("\n" + "Chatbot: " + resposta_user)
                return " Ahhh agora eu entendi, agora eu saquei, agora as peças se encaixaram"
def exiberesposta(resposta,nome):
    print(resposta.replace("Chatbot", nome))
    if resposta == "fim":
        return"fim"
    return"continua"