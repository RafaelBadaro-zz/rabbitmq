import pika
import sys


class Ativo:
    def __init__(self, qtd, nome_pregao, cod, atv_principal):
        self.qtd = qtd
        self.nome_pregao = nome_pregao
        self.cod = cod
        self.atv_principal = atv_principal

    def __repr__(self):
        return f"\nNome do Pregão: {self.nome_pregao},\nCódigo: {self.cod},\nAtividade Principal: {self.atv_principal}"\
               f"\n"


def carrega_ativos():
    ativos = []
    ativos.append(Ativo(300, 'AMBEV S/A ON', 'ABEV3', 'Fabricação e Distribuição de Cervejas. Refrigerantes e Bebidas '
                                                      'Não Carbonatadas e Não Alcoólicas.'))
    ativos.append(Ativo(300, 'PETROBRAS PN', 'PETR4', 'Petróleo. Gás e Energia'))
    ativos.append(Ativo(300, 'VALE PNA', 'VALE5', 'Mineração'))
    ativos.append(Ativo(300, 'ITAUUNIBANCO PN', 'ITUB4', 'A Sociedade Tem por Objeto A Atividade Bancária.'))
    ativos.append(Ativo(300, 'BRADESCO PN', 'BBDC4', 'Prática de Operações Bancárias em Geral. Inclusive Câmbio'))
    ativos.append(Ativo(300, 'BRASIL ON', 'BBAS3', 'Banco Múltiplo'))
    ativos.append(Ativo(300, 'CIELO ON', 'CIEL3', 'Empresa Prestadora de Serviços de Adquirência e Meios de '
                                                  'Pagamento.'))
    ativos.append(Ativo(300, 'PETROBRAS ON', 'PETR3', 'Petróleo. Gás e Energia.'))
    ativos.append(Ativo(300, 'HYPERMARCAS ON', 'HYPE3', 'Produção e Venda de Bens de Consumo e Medicamentos.'))
    ativos.append(Ativo(300, 'VALE ON', 'VALE3', 'Mineração'))
    ativos.append(Ativo(300, 'BBSEGURIDADE ON', 'BBSE3', 'Participação no Capital Social de Outras Sociedades. que '
                                                         'Tenham por Atividade Operações de Seguros. Resseguros. '
                                                         'Previdências Complementar ou Capitalização.'))
    ativos.append(Ativo(300, 'CETIP ON', 'CTIP3', 'Sociedade Administradora de Mercados de Balcão Organizados.'))
    ativos.append(Ativo(300, 'GERDAU PN', 'GGBR4', 'Participação e Adminsitração.'))
    ativos.append(Ativo(300, 'FIBRIA ON', 'FIBR3', ''))
    ativos.append(Ativo(300, 'RAIADROGASIL ON', 'RADL3', 'Comércio de Produtos Farmacêuticos. Perfumarias e Afins.'))
    return ativos
