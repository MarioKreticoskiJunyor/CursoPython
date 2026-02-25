# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, marca):
        self.marca = marca
        self._motor = None
        self._fabricante = None

    def inserir_motor(self,nome):
        self._motor = nome

    def inserir_fabricante(self,nome):
        self._fabricante = nome

    def mostrarmotor(self):
        print(f'{self.marca} possui motor {self._motor}')
    
    def mostrarfabricante(self):
        print(f'O carro {self.marca} e da fabricante {self._fabricante}')
    
    def mostrarcarro(self):
        print(f'O carro {self.marca} possui o motor {self._motor} e da fabricante {self._fabricante}')
        
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    


carro1 = Carro('Celta')
carro1.inserir_motor('1.0')
carro1.mostrarmotor()
carro1.inserir_fabricante('Chevrolet')
carro1.mostrarfabricante()
carro1.mostrarcarro()
