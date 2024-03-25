# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada Produto que herda de ABC (Abstract Base Class)
class Produto(ABC):
    # Método construtor da classe Produto, inicializando o nome, preço e quantidade em estoque do produto
    def __init__(self, nome, preco, quantidade_estoque):
        # Definindo atributo privado __nome
        self.__nome = nome
        # Definindo atributo privado __preco
        self.__preco = preco
        # Definindo atributo privado __quantidade_estoque
        self.__quantidade_estoque = quantidade_estoque
    
    # Definindo método abstrato exibir_informacoes()
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Método para calcular o total a ser pago pela quantidade específica do produto
    def calcular_total_venda(self, quantidade):
        return self.__preco * quantidade
    
    # Método para acessar o atributo privado __nome
    def get_nome(self):
        return self.__nome
    
    # Método para modificar o atributo privado __nome
    def set_nome(self, nome):
        self.__nome = nome
    
    # Método para acessar o atributo privado __preco
    def get_preco(self):
        return self.__preco
    
    # Método para modificar o atributo privado __preco
    def set_preco(self, preco):
        self.__preco = preco
    
    # Método para acessar o atributo privado __quantidade_estoque
    def get_quantidade_estoque(self):
        return self.__quantidade_estoque
    
    # Método para modificar o atributo privado __quantidade_estoque
    def set_quantidade_estoque(self, quantidade_estoque):
        self.__quantidade_estoque = quantidade_estoque

# Definindo classe Eletronico que herda de Produto
class Eletronico(Produto):
    # Método construtor da classe Eletronico
    def __init__(self, nome, preco, quantidade_estoque, garantia):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco, quantidade_estoque)
        # Definindo atributo privado __garantia
        self.__garantia = garantia
    
    # Implementação do método exibir_informacoes() para Eletronico
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Quantidade em estoque:", self.get_quantidade_estoque())
        print("Garantia:", self.__garantia)

# Definindo classe Roupa que herda de Produto
class Roupa(Produto):
    # Método construtor da classe Roupa
    def __init__(self, nome, preco, quantidade_estoque, tamanho, cor):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco, quantidade_estoque)
        # Definindo atributo privado __tamanho
        self.__tamanho = tamanho
        # Definindo atributo privado __cor
        self.__cor = cor
    
    # Implementação do método exibir_informacoes() para Roupa
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Quantidade em estoque:", self.get_quantidade_estoque())
        print("Tamanho:", self.__tamanho)
        print("Cor:", self.__cor)

# Definindo classe Alimento que herda de Produto
class Alimento(Produto):
    # Método construtor da classe Alimento
    def __init__(self, nome, preco, quantidade_estoque, data_validade, tipo):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco, quantidade_estoque)
        # Definindo atributo privado __data_validade
        self.__data_validade = data_validade
        # Definindo atributo privado __tipo
        self.__tipo = tipo
    
    # Implementação do método exibir_informacoes() para Alimento
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Quantidade em estoque:", self.get_quantidade_estoque())
        print("Data de Validade:", self.__data_validade)
        print("Tipo:", self.__tipo)

# Definindo função listar_produtos que recebe uma lista de objetos Produto
def listar_produtos(lista_produtos):
    # Iterando sobre cada produto na lista de produtos
    for produto in lista_produtos:
        # Chamando o método exibir_informacoes() do produto atual
        produto.exibir_informacoes()
        print()

# Exemplo de uso do código
# Criando instâncias de diferentes tipos de produtos
eletronico = Eletronico("Smartphone", 1500, 10, "1 ano")
roupa = Roupa("Camiseta", 30, 50, "M", "Azul")
alimento = Alimento("Arroz", 10, 100, "30/12/2024", "Grão")

# Criando uma lista contendo os objetos de produtos criados anteriormente
lista_produtos = [eletronico, roupa, alimento]

# Chamando a função listar_produtos para imprimir as informações de cada produto
listar_produtos(lista_produtos)
