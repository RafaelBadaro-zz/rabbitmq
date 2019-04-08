import pika
import sys

exchange_name = 'BOLSADEVALORES'
name = "BROKER"


# def compra(int quant, val real, char[] corretora)
# def venda(int quant, val real, char[] corretora)
# def info(char[] data)


def realiza_operacao(operacao):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare('BROKER', True, False, False, None)

    rota = operacao[0]
    mensagem = rota + '-' + operacao[1]

    channel.basic_publish(exchange='', routing_key='BROKER', body=mensagem)
    print(" [x] Enviado %r" % mensagem)

    connection.close()


def receber_notificacoes():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue

    binding_keys = sys.argv[1:]

    if not binding_keys:
        sys.stderr.write("Escreva a acao que deseja escutar: *.acao...\n")
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=binding_key)

    print('[*] Escutando  . Para sair pressione CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    # TODO - chamar um channel.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
