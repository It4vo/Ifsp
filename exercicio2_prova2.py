# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada Produto que herda de ABC (Abstract Base Class)
class Produto(ABC):
    # Método construtor da classe Produto, inicializando a marca, modelo e preço do produto
    def __init__(self, marca, modelo, preco):
        # Definindo atributo privado __marca
        self.__marca = marca
        # Definindo atributo privado __modelo
        self.__modelo = modelo
        # Definindo atributo privado __preco
        self.__preco = preco
    
    # Definindo método abstrato exibir_informacoes()
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Definindo método abstrato calcular_garantia()
    @abstractmethod
    def calcular_garantia(self):
        pass
    
    # Método para acessar o atributo privado __marca
    def get_marca(self):
        return self.__marca
    
    # Método para modificar o atributo privado __marca
    def set_marca(self, marca):
        self.__marca = marca
    
    # Método para acessar o atributo privado __modelo
    def get_modelo(self):
        return self.__modelo
    
    # Método para modificar o atributo privado __modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    # Método para acessar o atributo privado __preco
    def get_preco(self):
        return self.__preco
    
    # Método para modificar o atributo privado __preco
    def set_preco(self, preco):
        self.__preco = preco

# Definindo classe Geladeira que herda de Produto
class Geladeira(Produto):
    # Método construtor da classe Geladeira
    def __init__(self, marca, modelo, preco, capacidade):
        # Chamando o método construtor da classe pai
        super().__init__(marca, modelo, preco)
        # Definindo atributo privado __capacidade
        self.__capacidade = capacidade
    
    # Implementação do método exibir_informacoes() para Geladeira
    def exibir_informacoes(self):
        print("Marca:", self.get_marca())
        print("Modelo:", self.get_modelo())
        print("Preço:", self.get_preco())
        print("Capacidade:", self.__capacidade)
    
    # Implementação do método calcular_garantia() para Geladeira
    def calcular_garantia(self):
        # Considerando 1 ano de garantia para geladeiras
        return 1

# Definindo classe Televisor que herda de Produto
class Televisor(Produto):
    # Método construtor da classe Televisor
    def __init__(self, marca, modelo, preco, polegadas):
        # Chamando o método construtor da classe pai
        super().__init__(marca, modelo, preco)
        # Definindo atributo privado __polegadas
        self.__polegadas = polegadas
    
    # Implementação do método exibir_informacoes() para Televisor
    def exibir_informacoes(self):
        print("Marca:", self.get_marca())
        print("Modelo:", self.get_modelo())
        print("Preço:", self.get_preco())
        print("Polegadas:", self.__polegadas)
    
    # Implementação do método calcular_garantia() para Televisor
    def calcular_garantia(self):
        # Considerando 2 anos de garantia para televisores
        return 2

# Definindo classe MaquinaLavar que herda de Produto
class MaquinaLavar(Produto):
    # Método construtor da classe MaquinaLavar
    def __init__(self, marca, modelo, preco, capacidade_carga):
        # Chamando o método construtor da classe pai
        super().__init__(marca, modelo, preco)
        # Definindo atributo privado __capacidade_carga
        self.__capacidade_carga = capacidade_carga
    
    # Implementação do método exibir_informacoes() para MaquinaLavar
    def exibir_informacoes(self):
        print("Marca:", self.get_marca())
        print("Modelo:", self.get_modelo())
        print("Preço:", self.get_preco())
        print("Capacidade de Carga:", self.__capacidade_carga)
    
    # Implementação do método calcular_garantia() para MaquinaLavar
    def calcular_garantia(self):
        # Considerando 3 anos de garantia para máquinas de lavar
        return 3

# Definindo função listar_produtos que recebe uma lista de objetos Produto
def listar_produtos(lista_produtos):
    # Iterando sobre cada produto na lista de produtos
    for produto in lista_produtos:
        # Chamando o método exibir_informacoes() do produto atual
        produto.exibir_informacoes()
        # Imprimindo uma linha em branco para separar as informações de cada produto
        print()

# Exemplo de uso:
# Criando instâncias de diferentes tipos de produtos
geladeira = Geladeira("Brastemp", "BRM44", 2500.00, "500 litros")
televisor = Televisor("Samsung", "UN50TU8000", 3000.00, "50 polegadas")
maquina_lavar = MaquinaLavar("Electrolux", "LFE11", 2000.00, "11 kg")

# Criando uma lista contendo os objetos de produtos criados anteriormente
lista_produtos = [geladeira, televisor, maquina_lavar]

# Chamando a função listar_produtos para imprimir as informações de cada produto
listar_produtos(lista_produtos)
