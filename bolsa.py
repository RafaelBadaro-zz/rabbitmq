import pika
import sys

exchange_name = 'BOLSADEVALORES'


def enviar_notificacoes(operacao, acao):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    rota = '<' + operacao + '.' + acao + '>'
    mensagem = rota #TODO - adicionar a mensagem

    channel.basic_publish(exchange= exchange_name, routing_key=mensagem, body=mensagem)

    print(" [x] Enviado %r:%r" % mensagem)

    connection.close()


def receber_operacoes():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queueDeclare("BROKER", True, False, False, None)
    print("[*] Recebendo operacoes . Para sair pressione CTRL+C'")


    channel.basic_consume(queue='BROKER', on_message_callback=callback)


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    #TODO - chamar um metodo para realizar a operacao




