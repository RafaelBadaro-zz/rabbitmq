import bolsa

transacoes = [str]

def ler_transacao(data: str, acao: str):
    retorno = ""
    for item in transacoes:
        aux = item.split(";")
        if(aux[1] == acao and aux[0] == data):
            if(transacoes.index(item) == len(transacoes)):
                retorno += "<Transacao" + transacoes.index(item)+1 + "=" + item + ">"
            else:
                retorno += "<Transacao" + transacoes.index(item)+1 + "=" + item + ">,"
    return retorno


def enviar_transacao(transacao: str):
    aux = transacao.split(";")
    mensagem = aux[2] + ";" + aux[3]
    topico = "transacao." + aux[1]
    bolsa.enviar_notificacoes([topico, mensagem])


def gravar_transacao (transacao: str):
    transacoes.insert(transacao)
    enviar_transacao(transacao)
