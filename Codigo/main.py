from Codigo import broker

if __name__ == '__main__':
    opcao: str = -1

    corretora: broker

while(opcao != "0"):
    print("Selecione a operação desejada")
    print("1: Comprar")
    print("2: Vender")
    print("3: Informações")
    print("4: Monitorar ações")
    print("0: Sair")

    opcao = input()

    if(opcao == "1"):
        codigo = input("Digite o código da ação que deseja comprar, ex: PETR4")

        quantidade = input("Digite a quantidade de ações que deseja comprar, ex: 100")

        valor = input("Digite o valor pelo qual deseja comprar as ações, ex: 26.50")
        corretora.realiza_operacao(["compra."+codigo, quantidade, valor, corretora.name])

    elif (opcao == "2"):
        codigo = input("Digite o código da ação que seja vender, ex: PETR4")

        quantidade = input("Digite a quantidade de ações que deseja vender, ex: 100")

        valor = input("Digite o valor pelo qual deseja vender as ações, ex: 26.50")

        corretora.realiza_operacao(["venda."+codigo, quantidade, valor, corretora.name])

    elif(opcao == "3"):
        codigo = input("Digite o código da ação que deseja obter informações, ex: PETR4")

        data = input("Digite a dara e a hora, ex:17/01/19 22:35")

        corretora.realiza_operacao(["info." + codigo, data])

    elif(opcao == "4"):
        codigo = input("Digite o código da ação que deseja monitorar")

    else:
        print("Opção inválida, digite uma opção válida")
