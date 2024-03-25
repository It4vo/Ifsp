# Importando o módulo ABC (Abstract Base Classes) da biblioteca abc (Abstract Base Classes)
from abc import ABC, abstractmethod

# Definindo uma classe abstrata chamada Funcionario que herda de ABC (Abstract Base Class)
class Funcionario(ABC):
    # Método construtor da classe Funcionario, inicializando o nome e o salário base do funcionário
    def __init__(self, nome, salario_base):
        # Definindo atributo privado __nome
        self.__nome = nome
        # Definindo atributo privado __salario_base
        self.__salario_base = salario_base
    
    # Definindo método abstrato calcular_salario()
    @abstractmethod
    def calcular_salario(self):
        pass
    
    # Método para acessar o atributo privado __nome
    def get_nome(self):
        return self.__nome
    
    # Método para modificar o atributo privado __nome
    def set_nome(self, nome):
        self.__nome = nome
    
    # Método para acessar o atributo privado __salario_base
    def get_salario_base(self):
        return self.__salario_base
    
    # Método para modificar o atributo privado __salario_base
    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base

# Definindo classe FuncionarioRegular que herda de Funcionario
class FuncionarioRegular(Funcionario):
    # Implementação do método calcular_salario() para FuncionarioRegular
    def calcular_salario(self):
        return self.get_salario_base()

# Definindo classe Gerente que herda de Funcionario
class Gerente(Funcionario):
    # Método construtor da classe Gerente
    def __init__(self, nome, salario_base, bonus):
        # Chamando o método construtor da classe pai
        super().__init__(nome, salario_base)
        # Definindo atributo privado __bonus
        self.__bonus = bonus
    
    # Implementação do método calcular_salario() para Gerente
    def calcular_salario(self):
        return self.get_salario_base() + self.__bonus
    
    # Método para acessar o atributo privado __bonus
    def get_bonus(self):
        return self.__bonus
    
    # Método para modificar o atributo privado __bonus
    def set_bonus(self, bonus):
        self.__bonus = bonus

# Definindo classe Diretor que herda de Funcionario
class Diretor(Funcionario):
    # Método construtor da classe Diretor
    def __init__(self, nome, salario_base, participacao_lucros):
        # Chamando o método construtor da classe pai
        super().__init__(nome, salario_base)
        # Definindo atributo privado __participacao_lucros
        self.__participacao_lucros = participacao_lucros
    
    # Implementação do método calcular_salario() para Diretor
    def calcular_salario(self):
        return self.get_salario_base() + self.__participacao_lucros
    
    # Método para acessar o atributo privado __participacao_lucros
    def get_participacao_lucros(self):
        return self.__participacao_lucros
    
    # Método para modificar o atributo privado __participacao_lucros
    def set_participacao_lucros(self, participacao_lucros):
        self.__participacao_lucros = participacao_lucros

# Definindo função calcular_folha_pagamento que recebe uma lista de objetos Funcionario
def calcular_folha_pagamento(lista_funcionarios):
    # Inicializando variável total_folha com valor 0
    total_folha = 0
    # Iterando sobre cada funcionário na lista de funcionários
    for funcionario in lista_funcionarios:
        # Somando o salário do funcionário à variável total_folha
        total_folha += funcionario.calcular_salario()
    # Retornando o total da folha de pagamento
    return total_folha

# Exemplo de uso do código
# Criando instâncias de diferentes tipos de funcionários
funcionario_regular = FuncionarioRegular("João", 2000)
gerente = Gerente("Maria", 3000, 500)
diretor = Diretor("Carlos", 5000, 1000)

# Criando uma lista contendo os objetos de funcionários criados anteriormente
lista_funcionarios = [funcionario_regular, gerente, diretor]

# Chamando a função calcular_folha_pagamento para calcular o total da folha de pagamento
total_folha_pagamento = calcular_folha_pagamento(lista_funcionarios)

# Imprimindo o total da folha de pagamento
print("Total da folha de pagamento:", total_folha_pagamento)
