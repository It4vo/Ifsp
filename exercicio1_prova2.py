# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada MaterialDigital que herda de ABC (Abstract Base Class)
class MaterialDigital(ABC):
    # Método construtor da classe MaterialDigital, inicializando o título, autor e formato do material digital
    def __init__(self, titulo, autor, formato):
        # Definindo atributo privado __titulo
        self.__titulo = titulo
        # Definindo atributo privado __autor
        self.__autor = autor
        # Definindo atributo privado __formato
        self.__formato = formato
    
    # Definindo método abstrato exibir_informacoes()
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Definindo método abstrato calcular_tamanho()
    @abstractmethod
    def calcular_tamanho(self):
        pass
    
    # Método para acessar o atributo privado __titulo
    def get_titulo(self):
        return self.__titulo
    
    # Método para modificar o atributo privado __titulo
    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    # Método para acessar o atributo privado __autor
    def get_autor(self):
        return self.__autor
    
    # Método para modificar o atributo privado __autor
    def set_autor(self, autor):
        self.__autor = autor
    
    # Método para acessar o atributo privado __formato
    def get_formato(self):
        return self.__formato
    
    # Método para modificar o atributo privado __formato
    def set_formato(self, formato):
        self.__formato = formato

# Definindo classe Ebook que herda de MaterialDigital
class Ebook(MaterialDigital):
    # Método construtor da classe Ebook
    def __init__(self, titulo, autor, formato, numero_paginas):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, autor, formato)
        # Definindo atributo privado __numero_paginas
        self.__numero_paginas = numero_paginas
    
    # Implementação do método exibir_informacoes() para Ebook
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("Formato:", self.get_formato())
        print("Número de Páginas:", self.__numero_paginas)
    
    # Implementação do método calcular_tamanho() para Ebook
    def calcular_tamanho(self):
        # Considerando um tamanho médio de 0.1 MB por página
        return self.__numero_paginas * 0.1

# Definindo classe Audiolivro que herda de MaterialDigital
class Audiolivro(MaterialDigital):
    # Método construtor da classe Audiolivro
    def __init__(self, titulo, autor, formato, duracao):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, autor, formato)
        # Definindo atributo privado __duracao
        self.__duracao = duracao
    
    # Implementação do método exibir_informacoes() para Audiolivro
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("Formato:", self.get_formato())
        print("Duração:", self.__duracao, "horas")
    
    # Implementação do método calcular_tamanho() para Audiolivro
    def calcular_tamanho(self):
        # Considerando uma taxa de compressão de 1 MB por minuto
        return self.__duracao * 60

# Definindo classe DocumentoPDF que herda de MaterialDigital
class DocumentoPDF(MaterialDigital):
    # Método construtor da classe DocumentoPDF
    def __init__(self, titulo, autor, formato, tamanho_pagina):
        # Chamando o método construtor da classe pai
        super().__init__(titulo, autor, formato)
        # Definindo atributo privado __tamanho_pagina
        self.__tamanho_pagina = tamanho_pagina
    
    # Implementação do método exibir_informacoes() para DocumentoPDF
    def exibir_informacoes(self):
        print("Título:", self.get_titulo())
        print("Autor:", self.get_autor())
        print("Formato:", self.get_formato())
        print("Tamanho da Página:", self.__tamanho_pagina)
    
    # Implementação do método calcular_tamanho() para DocumentoPDF
    def calcular_tamanho(self):
        # Considerando um tamanho fixo de 1 MB por página
        return self.__tamanho_pagina

# Definindo função listar_materiais que recebe uma lista de objetos MaterialDigital
def listar_materiais(lista_materiais):
    # Iterando sobre cada material na lista de materiais
    for material in lista_materiais:
        # Chamando o método exibir_informacoes() do material atual
        material.exibir_informacoes()
        # Imprimindo uma linha em branco para separar as informações de cada material
        print()

# Exemplo de uso:
# Criando instâncias de diferentes tipos de materiais digitais
ebook = Ebook("Python Programming", "Guido van Rossum", "EPUB", 300)
audiolivro = Audiolivro("The Hobbit", "J.R.R. Tolkien", "MP3", 8)
pdf = DocumentoPDF("Machine Learning Basics", "Andrew Ng", "PDF", 2)

# Criando uma lista contendo os objetos de materiais digitais criados anteriormente
lista_materiais = [ebook, audiolivro, pdf]

# Chamando a função listar_materiais para imprimir as informações de cada material
listar_materiais(lista_materiais)
