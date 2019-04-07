import bolsa

transacoes = [str]

def enviar_transacao(transacao: str):
    aux = transacao.split(";")
    mensagem = aux[2] + ";" + aux[3]
    topico = "transacao." + aux[1]
    #bolsa.enviar_notificacoes(new str[]{topico, mensagem})

def gravar_transacao (transacao: str):
    transacoes.insert(transacao)
    enviar_transacao(transacao)