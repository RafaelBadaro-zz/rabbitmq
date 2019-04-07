import pika
import sys
import re

exchange_name = 'BOLSADEVALORES'


def enviar_notificacoes(topicos: list[str]):
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


#def tratar_msg(mensagem: str):



