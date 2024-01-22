# Operadores em e não em
# Strings são iteráveis
# 0 1 2 3 4 5
# O tá vio See More
# # -6-5-4-3-2-1
# nome  = 'Mario'
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])
# print(nome[4])
# print('Mar' in nome )
# print('z' in nome )
# print(10*'-')
# print('Mar' not in nome )
# print('zero' not in nome )
nome = input('Digite seu nome: ')
encontrar=input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:    
    print(f'{encontrar} nao esta em {nome}')