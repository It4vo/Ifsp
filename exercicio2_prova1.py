# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada Funcionario que herda de ABC (Abstract Base Class)
class Funcionario(ABC):
    # Método construtor da classe Funcionario, inicializando o nome, idade e salário do funcionário
    def __init__(self, nome, idade, salario):
        # Definindo atributo privado __nome
        self.__nome = nome
        # Definindo atributo privado __idade
        self.__idade = idade
        # Definindo atributo privado __salario
        self.__salario = salario
    
    # Definindo método abstrato exibir_informacoes()
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Método para calcular o bônus do funcionário
    def calcular_bonus(self):
        return 0
    
    # Método para acessar o atributo privado __nome
    def get_nome(self):
        return self.__nome
    
    # Método para modificar o atributo privado __nome
    def set_nome(self, nome):
        self.__nome = nome
    
    # Método para acessar o atributo privado __idade
    def get_idade(self):
        return self.__idade
    
    # Método para modificar o atributo privado __idade
    def set_idade(self, idade):
        self.__idade = idade
    
    # Método para acessar o atributo privado __salario
    def get_salario(self):
        return self.__salario
    
    # Método para modificar o atributo privado __salario
    def set_salario(self, salario):
        self.__salario = salario

# Definindo classe Desenvolvedor que herda de Funcionario
class Desenvolvedor(Funcionario):
    # Método construtor da classe Desenvolvedor
    def __init__(self, nome, idade, salario, linguagem_programacao):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, salario)
        # Definindo atributo privado __linguagem_programacao
        self.__linguagem_programacao = linguagem_programacao
    
    # Implementação do método exibir_informacoes() para Desenvolvedor
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Cargo: Desenvolvedor")
        print("Linguagem de Programação:", self.__linguagem_programacao)
    
    # Método para calcular o bônus do Desenvolvedor
    def calcular_bonus(self):
        return self.get_salario() * 0.1

# Definindo classe GerenteProjeto que herda de Funcionario
class GerenteProjeto(Funcionario):
    # Método construtor da classe GerenteProjeto
    def __init__(self, nome, idade, salario, projetos_gerenciados):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, salario)
        # Definindo atributo privado __projetos_gerenciados
        self.__projetos_gerenciados = projetos_gerenciados
    
    # Implementação do método exibir_informacoes() para GerenteProjeto
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Cargo: Gerente de Projeto")
        print("Projetos Gerenciados:", self.__projetos_gerenciados)
    
    # Método para calcular o bônus do GerenteProjeto
    def calcular_bonus(self):
        return self.get_salario() * 0.15

# Definindo classe AnalistaQualidade que herda de Funcionario
class AnalistaQualidade(Funcionario):
    # Método construtor da classe AnalistaQualidade
    def __init__(self, nome, idade, salario, metodologia_testes):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, salario)
        # Definindo atributo privado __metodologia_testes
        self.__metodologia_testes = metodologia_testes
    
    # Implementação do método exibir_informacoes() para AnalistaQualidade
    def exibir_informacoes(self):
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Cargo: Analista de Qualidade")
        print("Metodologia de Testes:", self.__metodologia_testes)
    
    # Método para calcular o bônus do AnalistaQualidade
    def calcular_bonus(self):
        return self.get_salario() * 0.12

# Definindo função listar_funcionarios que recebe uma lista de objetos Funcionario
def listar_funcionarios(lista_funcionarios):
    # Iterando sobre cada funcionário na lista de funcionários
    for funcionario in lista_funcionarios:
        # Chamando o método exibir_informacoes() do funcionário atual
        funcionario.exibir_informacoes()
        # Calculando e imprimindo o bônus do funcionário atual
        print("Bônus:", funcionario.calcular_bonus())
        print()

# Exemplo de uso do código
# Criando instâncias de diferentes tipos de funcionários
desenvolvedor = Desenvolvedor("João", 30, 5000, "Python")
gerente = GerenteProjeto("Maria", 35, 7000, ["Projeto A", "Projeto B"])
analista = AnalistaQualidade("Carlos", 28, 4500, "Scrum")

# Criando uma lista contendo os objetos de funcionários criados anteriormente
lista_funcionarios = [desenvolvedor, gerente, analista]

# Chamando a função listar_funcionarios para imprimir as informações de cada funcionário
listar_funcionarios(lista_funcionarios)
