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
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor

    def mostrarcarro(self):
        print(f'O carro {self.marca} possui o motor {self._motor} e da fabricante {self._fabricante}')
        
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    

fusca = Carro('Fusca')
volkswagen = Fabricante('volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor  = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
volkswagen = Fabricante('volkswagen')
motor_1_0 = Motor('1.0')
gol.fabricante = volkswagen
gol.motor  = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

uno = Carro('Uno')
fiat = Fabricante('fiat')
motor_1_0 = Motor('1.0')
uno.fabricante = fiat
uno.motor  = motor_1_0
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor  = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)