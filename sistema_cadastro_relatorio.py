#Gerenciador de Produtos e Fabricantes
produtos_lista = []
fabricantes_nomes = []
fabricantes_lista = []
dds = ['68', '82', '96', '92', '97', '71', '73', '74', '75', '77', '85', '88', '61', '27', '28', '62', '64', '98', '99',
       '65', '66', '67', '31', '32', '33', '34', '35', '37', '38', '91', '93', '94', '83', '41', '42', '43', '44', '45',
       '46', '81', '87', '86', '89', '21', '22', '24', '84', '51', '53', '54', '55', '69', '95', '47', '48', '49', '11',
       '12', '13', '14', '15', '16', '17', '18', '19', '79', '63']
UFS =['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
                          'PB',
                          'PR',
                          'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
class Produtos:
    def __init__(self, descricao, peso, valor_compra, valor_venda, fabricante):
        self.descricao = descricao
        self.peso = peso
        self.valor_compra = valor_compra
        self.valor_venda = valor_venda
        self.fabricante = fabricante
        self.valor_lucro = valor_compra - valor_venda
        self.percentual_lucro = round(((self.valor_venda - self.valor_compra) / self.valor_compra) * 100, 2)


class Fabricantes:
    def __init__(self, nome, site, telefone, uf):
        self.nome = nome
        self.site = site
        self.telefone = telefone
        self.uf = uf