# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'


if hasattr(string, metodo):
    print(getattr(string, metodo))
    print(string)
else: 
    print('Não existe o método',metodo)