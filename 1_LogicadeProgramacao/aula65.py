"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

#exercicio realizado por mim
# cpf = [7, 4, 6, 8, 2, 4, 8, 9, 0]
# print(f'CPF: ',*cpf, sep='')
# cont= 10
# soma = 0
# soma_ant = 0
# for indice in cpf:
#     if cont > 2:
#         soma = indice * cont
#         soma_ant=soma_ant + soma
#         cont -= 1 
#         print(F'{indice} * {cont} = {soma}')
#     else:
#         print(f'Total:',soma_ant)
# soma_ant *= 10 
# soma_ant %= 11

# if soma_ant >9 :
#     print('O primeiro dígito do CPF é 0')
# else:
#     print(f'O primeiro dígito do CPF é ',soma_ant)


#Primeiro exercico com o primeiro digito
cpf_enviado_pelo_usuario = '74682489070'
nove_digitos = cpf_enviado_pelo_usuario[:9]


cont_1= 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * cont_1
    cont_1 -= 1 
    
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0
print(f'O primeiro dígito do CPF é ',digito_1 )


#Segundo exercico com o segundo digito
dez_digitos = nove_digitos +str(digito_1)
cont_2= 11
resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * cont_2
    cont_2 -= 1 
    
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2  <=9 else 0

print(f'O segundo dígito do CPF é ',digito_2 )

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_pelo_usuario} é valido' )
else:
    print(f'CPF é invalido' )

