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

def cadastrar_fabricante():
    while True:
        while True:
            nome = input("Qual o nome do fabricante?")
            if len(nome) <= 0:
                print("Nome invalido")
            else:
                nome = nome
                break
        while True:
            site = input("Qual o site do fabricante?")
            if len(site) < 1 or len(site) > 63:
                print("Tamanho inválido")
            elif site.split()[0] == "-" or site.split()[-1] == '-':
                print("Formato incorreto")
            else:
                break
        while True:
            telefone = input("Qual o telefone do fabricante?")
            if len(telefone) < 8 or len(telefone) > 11:
                print("Tamanho de número incorreto")
            elif telefone[:2] not in dds:
                print("DDD do telefone inexistente!")
            else:
                break
        while True:
            uf = input("Qual o UF(Estado) do fabricante?").upper()
            if uf not in UFS:
                print("UF incorreta, tente novamente!")
            else:
                break
        break
    cadastro_fabr = Fabricantes(nome, site, telefone, uf)
    fabricantes_nomes.append(cadastro_fabr.nome)
    fabricantes_lista.append(cadastro_fabr)
    return cadastro_fabr


def cadastrar_produto():
    while True:
        descricao = input("Nome do produto:")
        while True:
            try:
                peso = float(input("Peso do produto em gramas: "))
                if peso < 0:
                    print("Peso incorreto")
                elif peso < 50 or peso > 50000:
                    print("Peso fora do limite permitido")
                else:
                    break
            except ValueError:
                print("Erro: o valor inserido não é um número válido")
            else:
                peso = peso
        while True:
            try:
                valor_compra = float(input("Valor de compra:"))
                if valor_compra < 0:
                    print("Valor incorreto")
                elif valor_compra < 0.50 or valor_compra > 8000:
                    print("Valor de compra fora do limite permitido")
                else:
                    break
            except ValueError:
                print("Erro: Valor incorreto")
            else:
                valor_compra = valor_compra
        while True:
            try:
                valor_venda = float(input("Valor de venda:"))
                if valor_venda < 0:
                    print("Valor incorreto")
                elif valor_venda < valor_compra:
                    print("Valor de compra é menor")
                elif valor_venda < 1 or valor_venda > 10000:
                    print("Valor de venda fora do limite permitido")
                else:
                    break
            except ValueError:
                print("Erro: Valor incorreto")
            else:
                valor_venda = valor_venda
        while True:
            try:
                nome_fabricante = input("Nome do fabricante:")
                if nome_fabricante not in fabricantes_nomes:
                    print("Fabricante inexistente ou incorreto")
                    print(f"Fabricantes: {fabricantes_nomes}")
                else:
                    break
            except ValueError:
                print("Erro: Valor incorreto")
            else:
                nome_fabricante = nome_fabricante
        break
    cadastro_produto = Produtos(descricao, peso, valor_compra, valor_venda, nome_fabricante)
    produtos_lista.append(cadastro_produto)
    return cadastro_produto