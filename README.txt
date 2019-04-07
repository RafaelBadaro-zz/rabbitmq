# RabbitMQ

Este projeto é uma implementação em Python de uma aplicação de publish-subscribe com RabbitMQ.

Para conseguir rodar a aplicação em sua máquina, alguns passos são necessários. Estes serão descritos a seguir.

1. Este projeto faz uso de Erlang/OTP 21 e RabbitMQ v3.7.14. Sua instalação deve ser feita de acordo com os tutoriais disponíveis em: https://www.rabbitmq.com/download.html.

2. A versão de Python utilizada é a 3.6.6 e a do pip é 19.0.3.

3. É necessário instalar uma dependência denominada Pika v1.0.0 em sua máquina para que a aplicação em Python consiga se integrar com o RabbitMQ. Você pode utilizar o pip para isto ou gerenciadores de dependências de sua preferência. Nós optamos por utilizar o Miniconda 3 (disponível em: https://docs.conda.io/en/latest/miniconda.html)

Após realizar estas configurações em seu ambiente, você deve ser capaz de rodar a aplicação como preferir.
