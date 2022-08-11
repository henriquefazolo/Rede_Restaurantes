class Lanche:
    def __init__(self):
        self.__nome = None
        self.__descricao = None
        self.__preco_venda = None
        self.__cod_lanche = None

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def preco_venda(self):
        return self.__preco_venda

    @property
    def cod_lanche(self):
        return self.__cod_lanche

    @cod_lanche.setter
    def cod_lanche(self, valor):
        self.__cod_lanche = valor

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @preco_venda.setter
    def preco_venda(self, preco):
        self.__preco_venda = preco


class RedeRestaurante:

    __rede = -1

    def __init__(self):
        self.__nome_rede = 'NecTronalds'
        self.__restaurantes_rede = []
        RedeRestaurante.__rede += 1

    @property
    def nome_rede(self):
        return self.__nome_rede

    @property
    def restaurantes_rede(self):
        return self.__restaurantes_rede

    @restaurantes_rede.setter
    def restaurantes_rede(self, restaurante):
        self.__restaurantes_rede += [restaurante]

    @staticmethod
    def quantidade_restaurantes():
        return RedeRestaurante.__rede

    def mostrar_cardapio_todos_paises(self):
        for i in self.__restaurantes_rede:
            i.mostrar_cardapio()

# rede contem rest
# class rede(rest)


class Restaurante:

    def __init__(self):
        self.__nome = None
        self.__cardapio = []
        self.__fator_moeda = None
        self.__nome_moeda = None
        self.rede = RedeRestaurante().nome_rede

    @property
    def nome(self):
        return self.__nome

    @property
    def cardapio(self):
        return self.__cardapio

    @property
    def fator_moeda(self):
        return self.__fator_moeda

    @property
    def nome_moeda(self):
        return self.__nome_moeda

    @nome.setter
    def nome(self, nome):
        self.__nome = f'{nome} - {self.rede}'

    @cardapio.setter
    def cardapio(self, item):
        self.__cardapio.append(item)

    @fator_moeda.setter
    def fator_moeda(self, fator):
        self.__fator_moeda = fator

    @nome_moeda.setter
    def nome_moeda(self, nome):
        self.__nome_moeda = nome

    def mostrar_cardapio(self):
        print(f'{self.nome} - Cardapio \n')
        for i in range(len(self.__cardapio)):
            print(f'{self.__cardapio[i].cod_lanche} - {self.__cardapio[i].nome} - {self.__cardapio[i].descricao} - '
                  f'{self.__cardapio[i].preco_venda * self.fator_moeda:.2f} - '
                  f'{self.nome_moeda}')
        print()

    def remover_item_cardapio(self, cod):
        for i in self.__cardapio:
            if i.cod_lanche == cod:
                print(f'Item {cod} removido.')
                self.__cardapio.remove(i)


# Criando a Rede
rede_nec_tronalds = RedeRestaurante()


# Criando os Restaurantes
brasil = Restaurante()
brasil.nome = 'Brasil'
brasil.fator_moeda = 5.10
brasil.nome_moeda = 'Real'
rede_nec_tronalds.restaurantes_rede = brasil

argentina = Restaurante()
argentina.nome = 'Argentina'
argentina.fator_moeda = 134.20
argentina.nome_moeda = 'Peso Argentido'
rede_nec_tronalds.restaurantes_rede = argentina

estados_unidos = Restaurante()
estados_unidos.nome = 'Estados Unidos'
estados_unidos.fator_moeda = 1
estados_unidos.nome_moeda = 'Dolar'
rede_nec_tronalds.restaurantes_rede = estados_unidos

japao = Restaurante()
japao.nome = 'Japão'
japao.fator_moeda = 132
japao.nome_moeda = 'Iene'
rede_nec_tronalds.restaurantes_rede = japao

# Criando Lanches
necfeijoada = Lanche()
necfeijoada.nome = 'NecFeijoada'
necfeijoada.descricao = 'Sabor Feijoada'
necfeijoada.preco_venda = 1
necfeijoada.cod_lanche = 101

necbacon = Lanche()
necbacon.nome = 'NecBacon'
necbacon.descricao = 'Sabor Bacon'
necbacon.preco_venda = 1.2
necbacon.cod_lanche = 102

necacaraje = Lanche()
necacaraje.nome = 'NecAcarajé'
necacaraje.descricao = 'Sabor Acarajé'
necacaraje.preco_venda = 1.5
necacaraje.cod_lanche = 103

necpicanha = Lanche()
necpicanha.nome = 'NecPicanha'
necpicanha.descricao = 'Sabor Picanha'
necpicanha.preco_venda = 2.5
necpicanha.cod_lanche = 104

necchimichurri = Lanche()
necchimichurri.nome = 'NecChimichurri'
necchimichurri.descricao = 'Sabor Chimichurri'
necchimichurri.preco_venda = 2.2
necchimichurri.cod_lanche = 105

necchedar = Lanche()
necchedar.nome = 'NecCheddar'
necchedar.descricao = 'Sabor Cheddar'
necchedar.preco_venda = 1.3
necchedar.cod_lanche = 106

necsushi = Lanche()
necsushi.nome = 'NecSushi'
necsushi.descricao = 'Sabor Sushi'
necsushi.preco_venda = 1.75
necsushi.cod_lanche = 107


# Criando Cardapio
brasil.cardapio = necfeijoada
brasil.cardapio = necbacon
brasil.cardapio = necacaraje
brasil.cardapio = necpicanha

argentina.cardapio = necpicanha
argentina.cardapio = necchimichurri

estados_unidos.cardapio = necbacon
estados_unidos.cardapio = necchedar

japao.cardapio = necsushi
japao.cardapio = necchedar

# Funcionalidade

rede_nec_tronalds.mostrar_cardapio_todos_paises()
brasil.mostrar_cardapio()
brasil.remover_item_cardapio(101)
brasil.mostrar_cardapio()
