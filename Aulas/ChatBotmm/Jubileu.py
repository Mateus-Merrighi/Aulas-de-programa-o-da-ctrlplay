import ProjetoChatBot as pc

nome_maquina= "Jubileu"


pc.saudacoes(nome_maquina)

while True: 
    texto= pc.recebaTexto()

    resposta= pc.buscaResposta(nome_maquina, texto)

    if pc.exiberesposta(resposta, nome_maquina) == 'fim':
        break