# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada Filme que herda de ABC (Abstract Base Class)
class Filme(ABC):
    # Método construtor da classe Filme, inicializando o título, diretor e ano de lançamento do filme
    def __init__(self, titulo, diretor, ano_lancamento):
        # Definindo atributo privado __titulo
        self.__titulo = titulo
        # Definindo atributo privado __diretor
        self.__diretor = diretor
        # Definindo atributo privado __ano_lancamento
        self.__ano_lancamento = ano_lancamento
    
    # Definindo método abstrato exibir_informacoes()
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Definindo método abstrato calcular_preco_locacao()
    @abstractmethod
    def calcular_preco_locacao(self, dias):
        pass
    
    # Método para acessar o atributo privado __titulo
    def get_titulo(self):
        return self.__titulo
    
    # Método para modificar o atributo privado __titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    # Método para acessar o atributo privado __diretor
    def get_diretor(self):
        return self.__diretor
    
    # Método para modificar o atributo privado __diretor
    def set_diretor(self, diretor):
        self.__diretor = diretor
    
    # Método para acessar o atributo privado __ano_lancamento
    def get_ano_lancamento(self):
        return self.__ano_lancamento
    
    # Método para modificar o atributo privado __ano_lancamento
    def set_ano_lancamento(self, ano_lancamento):
        self.__ano_lancamento = ano_lancamento

# Definindo classe Drama que herda de Filme
class Drama(Filme):
    # Método construtor da classe Drama
    def __init__(self, titulo, diretor, ano_lancamento, classificacao):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, diretor, ano_lancamento)
        # Definindo atributo privado __classificacao
        self.__classificacao = classificacao
    
    # Implementação do método exibir_informacoes() para Drama
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Diretor:", self.get_diretor())
        print("Ano de Lançamento:", self.get_ano_lancamento())
        print("Classificação:", self.__classificacao)
    
    # Implementação do método calcular_preco_locacao() para Drama
    def calcular_preco_locacao(self, dias):
        return dias * 2.5  # Preço fixo de locação para filmes de drama

# Definindo classe Comedia que herda de Filme
class Comedia(Filme):
    # Método construtor da classe Comedia
    def __init__(self, titulo, diretor, ano_lancamento, idade_minima):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, diretor, ano_lancamento)
        # Definindo atributo privado __idade_minima
        self.__idade_minima = idade_minima
    
    # Implementação do método exibir_informacoes() para Comedia
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Diretor:", self.get_diretor())
        print("Ano de Lançamento:", self.get_ano_lancamento())
        print("Idade Mínima:", self.__idade_minima)
    
    # Implementação do método calcular_preco_locacao() para Comedia
    def calcular_preco_locacao(self, dias):
        return dias * 3.0  # Preço fixo de locação para filmes de comédia

# Definindo classe Acao que herda de Filme
class Acao(Filme):
    # Método construtor da classe Acao
    def __init__(self, titulo, diretor, ano_lancamento, sequencia):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, diretor, ano_lancamento)
        # Definindo atributo privado __sequencia
        self.__sequencia = sequencia
    
    # Implementação do método exibir_informacoes() para Acao
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Diretor:", self.get_diretor())
        print("Ano de Lançamento:", self.get_ano_lancamento())
        print("Sequência:", self.__sequencia)
    
    def calcular_preco_locacao(self, dias):
        return dias * 3.5  # Preço fixo de locação para filmes de ação

def listar_filmes(lista_filmes):
    for filme in lista_filmes:
        filme.exibir_informacoes()
        print()

# Exemplo de uso:
drama = Drama("O Poderoso Chefão", "Francis Ford Coppola", 1972, "18 anos")
comedia = Comedia("Se Beber, Não Case!", "Todd Phillips", 2009, 16)
acao = Acao("John Wick", "Chad Stahelski", 2014, 1)

lista_filmes = [drama, comedia, acao]
listar_filmes(lista_filmes)