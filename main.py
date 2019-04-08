import broker

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
        broker.realiza_operacao(["compra."+codigo, quantidade, valor, broker.name])

    elif (opcao == "2"):
        codigo = input("Digite o código da ação que seja vender, ex: PETR4")

        quantidade = input("Digite a quantidade de ações que deseja vender, ex: 100")

        valor = input("Digite o valor pelo qual deseja vender as ações, ex: 26.50")

        broker.realiza_operacao(["venda."+codigo, quantidade, valor, broker.name])

    elif(opcao == "3"):
        codigo = input("Digite o código da ação que deseja obter informações, ex: PETR4")

    elif(opcao == "4"):
        print("Que saco")
    else:
        print("Opção inválida, digite uma opção válida")
