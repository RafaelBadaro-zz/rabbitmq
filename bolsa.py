import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


def fila_broker():
    print("Rodando fila BROKER")
    result = channel.queue_declare('BROKER', exclusive=True)
    queue_name = 'BROKER'

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write("Escreva a operacao e a acao que se deseja escutar : <operacao.acao>...\n")
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

    print(' [] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


# Canal que serve como pub
def fila_bolsa():
    print("Rodando fila BOLSA")
    result = channel.queue_declare('BOLSA', exclusive=True)
    queue_name = 'BOLSA'

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write("Escreva a operacao e a acao que se deseja escutar : <operacao.acao>...\n")
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(
            exchange='topic_logs', queue=queue_name, routing_key=binding_key)

    print(' [] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()
