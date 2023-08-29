"""
EXERCICIO DE WHILE
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])
contador = 0
nova_string =''

while contador < tamanho_nome:
    nova_string += f'*{nome[contador]}'
    contador += 1

print(f'{nova_string}')

#Soluçao professor
# nome = 'Maria Helena'  # Iteráveis

# indice = 0
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)