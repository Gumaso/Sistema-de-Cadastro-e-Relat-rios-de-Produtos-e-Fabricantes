# Gerenciador de Produtos e Fabricantes
produtos_lista = []
fabricantes_nomes = []
fabricantes_lista = []
dds = ['68', '82', '96', '92', '97', '71', '73', '74', '75', '77', '85', '88', '61', '27', '28', '62', '64', '98', '99',
       '65', '66', '67', '31', '32', '33', '34', '35', '37', '38', '91', '93', '94', '83', '41', '42', '43', '44', '45',
       '46', '81', '87', '86', '89', '21', '22', '24', '84', '51', '53', '54', '55', '69', '95', '47', '48', '49', '11',
       '12', '13', '14', '15', '16', '17', '18', '19', '79', '63']
UFS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
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


def listar_marcas():
    print("""
                ================================================
                RELATORIO 1 - LISTA DE TODAS AS MARCAS
                ================================================
                -------------+----------------+-------------------------------+-----------
                Marca        |   Site         | Telefone       | UF
    """)
    for item in fabricantes_lista:
        print(f"""
        -------------+----------------+-------------------------------+-----------
                {item.nome} | {item.site} | {item.telefone}            | {item.uf}
        """)
    return


def listar_produtos_uf():
    while True:
        estado = input("Qual estado?").upper()
        if estado not in UFS:
            print("Estado invalido!")
        else:
            break
    fabri_estados_nome = []
    for fabri in fabricantes_lista:
        if fabri.uf == estado:
            fabri_estados_nome.append(fabri.nome)

    print(f"PRODUTOS DO ESTADO {estado}")
    for produto in produtos_lista:
        if produto.fabricante in fabri_estados_nome:
            print(f"""
        |________________________________________+
        |Descrição: {produto.descricao}
        |Peso em gramas: {produto.peso}g
        |Valor de compra:R${produto.valor_compra:.2f}
        |Valor de venda: R${produto.valor_venda:.2f}
        |Fabricante: {produto.fabricante}
        +_______________________________________+""")


def listar_produtos_marca():
    marca = input("De qual marca deseja saber os produtos?")
    for produto in produtos_lista:
        if produto.fabricante == marca:
            print(f"""
                            +________________________________________+
                            |Descrição: {produto.descricao}|
                            |Peso em gramas: {produto.peso}g|
                            |Valor de compra:R${produto.valor_compra:.2f}|
                            |Valor de venda: R${produto.valor_venda:.2f}|
                            |Fabricante: {produto.fabricante}|
                            +_______________________________________+""")


def listar_produtos():
    for item in produtos_lista:
        print(f"""
        |________________________________________+
        |Descrição: {item.descricao}
        |Peso em kgs: {item.peso}
        |Valor de compra:R${item.valor_compra:.2f}
        |Valor de venda: R${item.valor_venda:.2f}
        |Fabricante: {item.fabricante}
        +_______________________________________+""")


def produto_mais_caro():
    global nome_fabr
    valores_produtos = {}
    estados = []
    for prod in produtos_lista:
        valores_produtos.update({prod.fabricante: prod.valor_venda})
    produto_maior_valor = max(valores_produtos.values())
    for fabri in fabricantes_lista:
        for chave, valor in valores_produtos.items():
            if valor == produto_maior_valor:
                nome_fabr = chave
        if fabri.nome == nome_fabr:
            estados.append(fabri.uf)
    print(f"Os estados com o(s) produto(s) mais caro são:")
    for estado in estados:
        print(f"UF: {estado} | Preço: R${produto_maior_valor}")


def produto_mais_barato():
    valores = []
    for prod in produtos_lista:
        valores.append(prod.valor_venda)
    valores_produto = {}
    for produto in produtos_lista:
        if produto.valor_venda == min(valores):
            item = {produto.valor_venda: produto.fabricante}
            valores_produto.update(item)
    print("Os fabricantes com os produtos mais barato são:")
    for fabricante in valores_produto.values():
        print(f"Fabricante: {fabricante}")


def crescente_valor_produto():
    valores = []
    for produto in produtos_lista:
        valores.append(produto.valor_venda)
    print("Valores dos produtos em ordem crescente")
    valores = sorted(valores)
    for valor in valores:
        print(f"R$: {valor:.2f}")


def crescente_valor_lucro_produto():
    lucro_produtos = []
    for x in produtos_lista:
        lucro_produtos.append(x.valor_venda - x.valor_compra)
    print("Valores dos lucros dos produtos em ordem crescente")
    lucro_produtos = sorted(lucro_produtos)
    for valor in lucro_produtos:
        print(f"R$: {valor:.2f}")


def crescente_valor_lucro_porcentagem_produto():
    lucro_produtos = []
    for x in produtos_lista:
        lucro_produtos.append(((x.valor_venda - x.valor_compra) / x.valor_compra) * 100)
    print("Valores percentuais dos lucros dos produtos em ordem crescente")
    lucro_produtos = sorted(lucro_produtos)
    for valor in lucro_produtos:
        print(f"{valor:.2f}%")


def marcas_descrecente():
    marcas_nomes = sorted(fabricantes_nomes, reverse=True)
    organizando = []
    for item in fabricantes_lista:
        for nome in marcas_nomes:
            if item.nome == nome:
                organizando.append(item)
    print("Marcas em ordem alfabetica descrescente")

    for marca in organizando:
        print(f"""
        Nome da marca: {marca.nome}
        Site: {marca.site}
        Telefone: {marca.telefone}
        UF: {marca.uf}""")


def produtos_crescente():
    produtos_nome = []
    for produt in produtos_lista:
        produtos_nome.append(produt.descricao)
    produtos_nome = sorted(produtos_nome)
    organizando = []
    for item in produtos_lista:
        for nome in produtos_nome:
            if item.descricao == nome:
                organizando.append(item)
    print("Produtos em ordem alfabetica crescente")
    for item in organizando:
        print(f"""
                |________________________________________+
                |Descrição: {item.descricao}
                |Peso em kgs: {item.peso}
                |Valor de compra:R${item.valor_compra:.2f}
                |Valor de venda: R${item.valor_venda:.2f}
                |Fabricante: {item.fabricante}
                +_______________________________________+""")


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

while True:
    if len(fabricantes_lista) < 2 or len(fabricantes_lista) > 5:
        print("Número inválido de fabricantes, necessário o cadastro!")
        cadas_fabri = cadastrar_fabricante()
    else:
        cadastrar = input("Deseja cadastrar um novo fabricante?[S]/[N]").upper()
        if cadastrar == 'S':
            cadas_fabri = cadastrar_fabricante()
        else:
            print()
    if len(produtos_lista) < 5 or len(produtos_lista) > 50:
        print("Número inválido de produtos, necessário o cadastro!")
        cadas_produt = cadastrar_produto()
    else:
        cadastrar2 = input('Deseja cadastrar um novo produto?[S]/[N]').upper()
        if cadastrar2 == 'S':
            cadas_produt = cadastrar_produto()
        else:
            print()
    opcao = int(input("""
                                         [0] Sair do programa
                                         [1] Listar todas as marcas
                                         [2] Listar todos os produtos
                                         [3] Listar os produtos de um determinado estado   
                                         [4] Listar os produtos de uma determinada marca  
                                         [5] Apresentar o(s) estado (s) onde está registrado o produto mais caro
                                         [6] Apresentar o(s) fabricante(s) onde está registrado o produto mais barato
                                         [7] Listar todos os produtos em ordem crescente de valor
                                         [8] Listar todos os produtos em ordem crescente de maior "valor do lucro"
                                         [9] Listar todos os produtos em ordem crescente de maior "percentual de lucro"
                                         _____________________________________________________________________________
                                         [10] Listar todos os produtos em ordem alfabética crescente A-Z
                                         [11] Listar todas as marcas em ordem alfabética decrescente Z-A
                                         """))
    if opcao == 0:
        print("Programa encerrado")
        break
    elif opcao == 1:
        listar_marcas()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        listar_produtos_uf()
    elif opcao == 4:
        listar_produtos_marca()
    elif opcao == 5:
        produto_mais_caro()
    elif opcao == 6:
        produto_mais_barato()
    elif opcao == 7:
        crescente_valor_produto()
    elif opcao == 8:
        crescente_valor_lucro_produto()
    elif opcao == 9:
        crescente_valor_lucro_porcentagem_produto()
    elif opcao == 10:
        produtos_crescente()
    elif opcao == 11:
        marcas_descrecente()
    else:
        print("Apenas números e entre 1 - 11")