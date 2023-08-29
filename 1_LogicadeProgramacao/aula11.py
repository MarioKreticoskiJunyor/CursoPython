# 1. (n + n)  primeiro o que tiver dentro de parenteses 
# 2. **       segundo o que estiver potenciação ou esponeciação
# 3. * / // % terceiro multiplicação "*", divisao"/", divisao inteira "//" e o moduilo "%" Serão execultada da esquerda para direita
# 4. + -      ultimo adição e subtração Serão execultada da esquerda para direita

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)