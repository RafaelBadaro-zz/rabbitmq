import pika
import sys
import re

exchange_name = 'BOLSADEVALORES'


def enviar_notificacoes(topicos):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    rota = topicos[0] # operacao.acao
    mensagem = topicos[1] # quant;val;corretora

    channel.basic_publish(exchange=exchange_name, routing_key=rota, body=mensagem)

    print(" [x] Enviado %r:%r" % rota, mensagem)

    connection.close()


def receber_operacoes():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queueDeclare("BROKER", True, False, False, None)
    print("[*] Recebendo operacoes . Para sair pressione CTRL+C'")

    channel.basic_consume(queue='BROKER', on_message_callback=callback)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    tratar_msg(body)


def tratar_msg(mensagem: str):
    #TODO - formtar para double

    msg_formatada = formata_msg(mensagem)

    operacao = msg_formatada[0]
    acao = msg_formatada[1]
    quant = msg_formatada[3]
    val = msg_formatada[5]
    corretora = msg_formatada[7]






def formata_msg(mensagem: str):
    nomes = re.compile('\W').split(mensagem)

    # nome é um vetor com os atributos da mensgem,isto é
    # nomes[0] = operacao Ex: venda
    # nomes[3] = quantidade(valor numérico)
    for s in nomes:  # remove espaços sem branco da
        if s == '':
            nomes.remove(s)

    return nomes;