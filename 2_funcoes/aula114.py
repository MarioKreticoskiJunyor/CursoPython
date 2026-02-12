# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm


# import sys 
# sys.setrecursionlimit(1004)

# def recursiva(inicio=0, fim=10):
#     print(inicio, fim)
#     #caso base
#     if inicio >=fim:
#         return fim
    
#     #caso recursivo 
#     #contar ate chegar ao final
#     inicio +=1
#     return recursiva(inicio,fim)

# print(recursiva(0,1900))

# for i in range(1,11):
#     print(i)


def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))

#ACIMA DE MIL DA PAU, PYTHON TEM LIMITE DE MIL, NAO E RECOMENDADO UTILZIAR SEMPRE
