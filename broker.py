import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')


def realiza_operacao(operacao, quant, val, corretora, acao):
    routing_key = operacao + '.' + acao
    message = '<quant: ' + quant + ', val: ' + val + ', corretora:' + corretora + '>'
    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message)
    print(" [x] Enviado %r:%r" % (routing_key, message))
    connection.close()


realiza_operacao('venda', '1', '25', 'inacio', 'petr4')
