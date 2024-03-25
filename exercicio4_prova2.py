# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada MembroEscola que herda de ABC (Abstract Base Class)
class MembroEscola(ABC):
    # Método construtor da classe MembroEscola, inicializando o nome, idade e matrícula do membro da escola
    def __init__(self, nome, idade, matricula):
        # Definindo atributo privado __nome para armazenar o nome do membro
        self.__nome = nome
        # Definindo atributo privado __idade para armazenar a idade do membro
        self.__idade = idade
        # Definindo atributo privado __matricula para armazenar a matrícula do membro
        self.__matricula = matricula
    
    # Definindo método abstrato exibir_informacoes() que deve ser implementado pelas classes filhas
    @abstractmethod
    def exibir_informacoes(self):
        pass
    
    # Definindo método abstrato calcular_taxa_mensalidade() que deve ser implementado pelas classes filhas
    @abstractmethod
    def calcular_taxa_mensalidade(self):
        pass
    
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
    
    # Método para acessar o atributo privado __matricula
    def get_matricula(self):
        return self.__matricula
    
    # Método para modificar o atributo privado __matricula
    def set_matricula(self, matricula):
        self.__matricula = matricula

# Definindo classe Aluno que herda de MembroEscola
class Aluno(MembroEscola):
    # Método construtor da classe Aluno
    def __init__(self, nome, idade, matricula, serie):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, matricula)
        # Definindo atributo privado __serie para armazenar a série do aluno
        self.__serie = serie
    
    # Implementação do método exibir_informacoes() para Aluno
    def exibir_informacoes(self):
        # Imprimindo informações do aluno
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Matrícula:", self.get_matricula())
        print("Série:", self.__serie)
    
    # Implementação do método calcular_taxa_mensalidade() para Aluno
    def calcular_taxa_mensalidade(self):
        # Implementação do cálculo da taxa de mensalidade para aluno
        # Aqui você pode adicionar a lógica de cálculo da taxa mensalidade específica para alunos
        pass

# Definindo classe Professor que herda de MembroEscola
class Professor(MembroEscola):
    # Método construtor da classe Professor
    def __init__(self, nome, idade, matricula, disciplina):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, matricula)
        # Definindo atributo privado __disciplina para armazenar a disciplina do professor
        self.__disciplina = disciplina
    
    # Implementação do método exibir_informacoes() para Professor
    def exibir_informacoes(self):
        # Imprimindo informações do professor
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Matrícula:", self.get_matricula())
        print("Disciplina:", self.__disciplina)
    
    # Implementação do método calcular_taxa_mensalidade() para Professor
    def calcular_taxa_mensalidade(self):
        # Implementação do cálculo da taxa de mensalidade para professor
        # Aqui você pode adicionar a lógica de cálculo da taxa mensalidade específica para professores
        pass

# Definindo classe FuncionarioAdministrativo que herda de MembroEscola
class FuncionarioAdministrativo(MembroEscola):
    # Método construtor da classe FuncionarioAdministrativo
    def __init__(self, nome, idade, matricula, cargo):
        # Chamando o método construtor da classe pai
        super().__init__(nome, idade, matricula)
        # Definindo atributo privado __cargo para armazenar o cargo do funcionário administrativo
        self.__cargo = cargo
    
    # Implementação do método exibir_informacoes() para FuncionarioAdministrativo
    def exibir_informacoes(self):
        # Imprimindo informações do funcionário administrativo
        print("Nome:", self.get_nome())
        print("Idade:", self.get_idade())
        print("Matrícula:", self.get_matricula())
        print("Cargo:", self.__cargo)
    
    # Implementação do método calcular_taxa_mensalidade() para FuncionarioAdministrativo
    def calcular_taxa_mensalidade(self):
        # Funcionários administrativos não pagam taxa de mensalidade
        return 0

# Definindo função listar_membros que recebe uma lista de objetos MembroEscola
def listar_membros(lista_membros):
    # Iterando sobre cada membro na lista de membros da escola
    for membro in lista_membros:
        # Chamando o método exibir_informacoes() do membro atual
        membro.exibir_informacoes()
        # Imprimindo uma linha em branco para separar as informações de cada membro
        print()

# Exemplo de uso:
# Criando instâncias de diferentes tipos de membros da escola
aluno = Aluno("João", 15, "2022001", "9º ano")
professor = Professor("Maria", 35, "P001", "Matemática")
funcionario_administrativo = FuncionarioAdministrativo("Carlos", 40, "F001", "Secretário")

# Criando uma lista contendo os objetos de membros da escola criados anteriormente
lista_membros = [aluno, professor, funcionario_administrativo]

# Chamando a função listar_membros para imprimir as informações de cada membro
listar_membros(lista_membros)
