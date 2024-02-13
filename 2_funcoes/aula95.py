#parte 3
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
#Try, execept, else e finally

try :
    print('Abrir o arquivo')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu zero')
except IndexError as error:
    print('IndexError')
except (NameError,ImportError) :
    print('NameError, ImportError')
else:
    print('Nao deu erro')
finally: 
    print('FECHAR ARQUIVO')
