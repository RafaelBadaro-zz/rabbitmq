# RabbitMQ

Este projeto é uma implementação em Python de uma aplicação de publish-subscribe com RabbitMQ.

Para conseguir rodar a aplicação em sua máquina, alguns passos são necessários. Estes serão descritos a seguir.

1. Este projeto faz uso de Erlang/OTP 21 e RabbitMQ v3.7.14. Sua instalação deve ser feita de acordo com os tutoriais
disponíveis em: https://www.rabbitmq.com/download.html.

2. A versão de Python utilizada é a 3.6.6 e a do pip é 19.0.3.

3. É necessário instalar uma dependência denominada Pika v1.0.0 em sua máquina para que a aplicação em Python consiga
se integrar com o RabbitMQ. Você pode utilizar o pip para isto ou gerenciadores de dependências/ambientes virtuais de
sua preferência. Nós optamos por utilizar o Miniconda 3 (disponível em: https://docs.conda.io/en/latest/miniconda.html).

    Exemplo de como montar o ambiente virtual como o Miniconda 3 (após instalação, via linha de comando):

        conda create -n rabbitmq
        conda install -n rabbitmq -c "conda-forge" python=3.6.6 pika=1.0.0

    OBS: no Linux, basta incluir o diretório bin do Miniconda na PATH, caso o instalador não tenha feito isso
         automaticamente. No Windows, estes comandos devem ser executados no Anaconda Prompt.

    Exemplos de como ativar o ambiente para a execução da aplicação via terminal:

        No Linux (terminal):

            source activate rabbitmq

        No Windows:

            conda activate rabbitmq

Feito isto, basta executar o código usando o comando python + os arquivos alvo no terminal.
