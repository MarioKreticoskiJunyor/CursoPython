#EXEMPLO DE USO DE SETS
letras = set()

while True:
    letra =input('Digite: ')
    letras.add(letra)
    if 'l' in letras:
        print('Parabens')
        break
    print(letras)
