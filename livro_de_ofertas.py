import pika
import sys


class Ativo:
    def __init__(self, nome_pregao, cod, atv_principal):
        self.nome_pregao = nome_pregao
        self.cod = cod
        self.atv_principal = atv_principal

    def __repr__(self):
        return f"\nNome do Pregão: {self.nome_pregao},\nCódigo: {self.cod},\nAtividade Principal: {self.atv_principal}"\
               f"\n"


def carrega_ativos():
    ativos = []
    ativos.append(Ativo('AMBEV S/A ON', 'ABEV3', 'Fabricação e Distribuição de Cervejas. Refrigerantes e Bebidas Não '
                                                 'Carbonatadas e Não Alcoólicas.'))
    ativos.append(Ativo('PETROBRAS PN', 'PETR4', 'Petróleo. Gás e Energia'))
    ativos.append(Ativo('VALE PNA', 'VALE5', 'Mineração'))
    ativos.append(Ativo('ITAUUNIBANCO PN', 'ITUB4', 'A Sociedade Tem por Objeto A Atividade Bancária.'))
    ativos.append(Ativo('BRADESCO PN', 'BBDC4', 'Prática de Operações Bancárias em Geral. Inclusive Câmbio'))
    ativos.append(Ativo('BRASIL ON', 'BBAS3', 'Banco Múltiplo'))
    ativos.append(Ativo('CIELO ON', 'CIEL3', 'Empresa Prestadora de Serviços de Adquirência e Meios de Pagamento.'))
    ativos.append(Ativo('PETROBRAS ON', 'PETR3', 'Petróleo. Gás e Energia.'))
    ativos.append(Ativo('HYPERMARCAS ON', 'HYPE3', 'Produção e Venda de Bens de Consumo e Medicamentos.'))
    ativos.append(Ativo('VALE ON', 'VALE3', 'Mineração'))
    ativos.append(Ativo('BBSEGURIDADE ON', 'BBSE3', 'Participação no Capital Social de Outras Sociedades. que Tenham '
                                                    'por Atividade Operações de Seguros. Resseguros. Previdências '
                                                    'Complementar ou Capitalização.'))
    ativos.append(Ativo('CETIP ON', 'CTIP3', 'Sociedade Administradora de Mercados de Balcão Organizados.'))
    ativos.append(Ativo('GERDAU PN', 'GGBR4', 'Participação e Adminsitração.'))
    ativos.append(Ativo('FIBRIA ON', 'FIBR3', ''))
    ativos.append(Ativo('RAIADROGASIL ON', 'RADL3', 'Comércio de Produtos Farmacêuticos. Perfumarias e Afins.'))
    return ativos
