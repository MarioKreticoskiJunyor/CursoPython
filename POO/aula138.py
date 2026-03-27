# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '1234'

    def __init__(self,nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_class(self):
        print('Eita, nem sai da classse')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'aluno'

c1 = Cliente('Luiz','Otavio')
c1.falar_nome_class()
a1 = Aluno('Maria','Helena')
a1.falar_nome_class()
print(a1.cpf)

# help(Cliente)
