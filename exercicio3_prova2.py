# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada ItemMenu que herda de ABC (Abstract Base Class)
class ItemMenu(ABC):
    # Método construtor da classe ItemMenu, inicializando o nome e o preço do item de menu
    def __init__(self, nome, preco):
        # Definindo atributo privado __nome para armazenar o nome do item
        self.__nome = nome
        # Definindo atributo privado __preco para armazenar o preço do item
        self.__preco = preco
    
    # Definindo método abstrato exibir_informacoes() que deve ser implementado pelas classes filhas
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Definindo método abstrato calcular_tempo_preparo() que deve ser implementado pelas classes filhas
    @abstractmethod
    def calcular_tempo_preparo(self):
        pass
    
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

# Definindo classe PratoPrincipal que herda de ItemMenu
class PratoPrincipal(ItemMenu):
    # Método construtor da classe PratoPrincipal
    def __init__(self, nome, preco, ingredientes):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco)
        # Definindo atributo privado __ingredientes para armazenar os ingredientes do prato principal
        self.__ingredientes = ingredientes
    
    # Implementação do método exibir_informacoes() para PratoPrincipal
    def exibir_informacoes(self):
        # Imprimindo informações do prato principal
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Ingredientes:", self.__ingredientes)
    
    # Implementação do método calcular_tempo_preparo() para PratoPrincipal
    def calcular_tempo_preparo(self):
        # Considerando 30 minutos de preparo para um prato principal
        return 30

# Definindo classe Bebida que herda de ItemMenu
class Bebida(ItemMenu):
    # Método construtor da classe Bebida
    def __init__(self, nome, preco, teor_alcoolico):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco)
        # Definindo atributo privado __teor_alcoolico para armazenar o teor alcoólico da bebida
        self.__teor_alcoolico = teor_alcoolico
    
    # Implementação do método exibir_informacoes() para Bebida
    def exibir_informacoes(self):
        # Imprimindo informações da bebida
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Teor Alcoólico:", self.__teor_alcoolico)
    
    # Implementação do método calcular_tempo_preparo() para Bebida
    def calcular_tempo_preparo(self):
        # Considerando 0 minutos de preparo para uma bebida
        return 0

# Definindo classe Sobremesa que herda de ItemMenu
class Sobremesa(ItemMenu):
    # Método construtor da classe Sobremesa
    def __init__(self, nome, preco, tipo):
        # Chamando o método construtor da classe pai
        super().__init__(nome, preco)
        # Definindo atributo privado __tipo para armazenar o tipo de sobremesa
        self.__tipo = tipo
    
    # Implementação do método exibir_informacoes() para Sobremesa
    def exibir_informacoes(self):
        # Imprimindo informações da sobremesa
        print("Nome:", self.get_nome())
        print("Preço:", self.get_preco())
        print("Tipo:", self.__tipo)
    
    # Implementação do método calcular_tempo_preparo() para Sobremesa
    def calcular_tempo_preparo(self):
        # Considerando 15 minutos de preparo para uma sobremesa
        return 15

# Definindo função listar_itens_menu que recebe uma lista de objetos ItemMenu
def listar_itens_menu(lista_itens):
    # Iterando sobre cada item na lista de itens de menu
    for item in lista_itens:
        # Chamando o método exibir_informacoes() do item atual
        item.exibir_informacoes()
        # Imprimindo uma linha em branco para separar as informações de cada item
        print()

# Exemplo de uso:
# Criando instâncias de diferentes tipos de itens de menu
prato_principal = PratoPrincipal("Feijoada", 25.00, ["Feijão", "Carne de Porco", "Linguiça", "Farofa", "Couve"])
bebida = Bebida("Caipirinha", 10.00, "Alta")
sobremesa = Sobremesa("Pudim", 8.00, "Doce de Leite")

# Criando uma lista contendo os objetos de itens de menu criados anteriormente
lista_itens = [prato_principal, bebida, sobremesa]

# Chamando a função listar_itens_menu para imprimir as informações de cada item
listar_itens_menu(lista_itens)
