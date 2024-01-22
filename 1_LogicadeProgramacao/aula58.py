"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    opcao = input('\nSelecione uma opção\n[i]nserir [a]apagar [l]istar:')
    if opcao == 'i':
        os.system('clear')
        inserir = input('valor:')
        lista.append(inserir)
    
    elif opcao == 'a':
        indice_str = input('informe o que gostaria de apagar:')
    
        try:
            indice = int(indice_str )
            del lista[indice]
    
        except ValueError:
            print('Por favor digite numero inteiro')
        except IndexError:
            print('Indice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    
    elif opcao == 'l':
        os.system('clear')
        if len(lista) == 0:
           print('Nada para listar')
        for indice,nome in enumerate(lista):
            print(indice,nome)
    else:
        print('Opção invalida, por favor escolha i,a ou l.')