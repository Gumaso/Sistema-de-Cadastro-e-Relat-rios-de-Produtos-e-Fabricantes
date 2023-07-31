#Gerenciador de Produtos e Fabricantes
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