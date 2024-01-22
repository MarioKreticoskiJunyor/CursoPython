nome = 'Mario Kreticoski Junyor'
altura  = 1.73
peso = 88
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

#f-strings formatação 
print(linha_1)
print(linha_2, linha_3)
