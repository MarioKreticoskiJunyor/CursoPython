# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os 
import json


### MINHA VERSAO COM JSON
###
# lista_tarefas = ["listar", "desfazer", "refazer","clear"]
# tudo = []
# refazer = []


# def bancojson():
#     with open('2_funcoes\\aula120zexecicio.json', 'w',encoding='utf8') as arquivo:
#         json.dump(
#             tudo, 
#             arquivo, 
#             ensure_ascii=False,
#             indent=2
#             )
#         return

# def listar():
#     if not tudo:
#         print(f'Não possui nenhuma tarefa')
#         return
#     else:
#         for i in tudo:
#             print(i)
#     print()

# def realizar(entrada):
#     tudo.append(entrada)
#     bancojson()
#     refazer.append(entrada)
#     listar()

# def excluir():
#     if not tudo:
#         print(f'Não possui nenhuma tarefa')
#         return
#     else:
#         tudo.pop()
#         bancojson()
#         return

# def refaz():
#     if not refazer:
#         print(f'Não possui nenhuma tarefa')
#         return
#     else:
#         tudo.append(refazer[-1])
#         bancojson()
#         listar()
#         return

# def comando(entrada):
#     if entrada.lower() in lista_tarefas:
#        if entrada.lower() == 'listar':
#            return listar()
#        if entrada.lower() == 'desfazer':
#            return excluir()
#        if entrada.lower() == 'refazer':
#            return refaz()
#        if entrada.lower() == 'clear':
#            return os.system('cls')
#     else:
#         realizar(entrada)
        
# while True:
#     print(f'Comandos:Listar, Desfazer e Refazer')
#     entrada = input(f'Digite uma tarefa ou comando:')
#     comando(entrada)



#forma do professor 


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)
def ler(tarefas,caminho_arquivo):
    dados = []
    try:        
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
            dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)


CAMINHO_ARQUIVO = '2_funcoes\\aula119.json'
tarefas = ler([] ,CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('clear')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
