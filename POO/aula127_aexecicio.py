# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'POO\\aula127z.json'

class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome =nome
        self.idade =idade


p1 = Pessoa('Mario', 25)
p2 = Pessoa('João', 22)
p3 = Pessoa('Maria', 12)

bd = [vars(p1),p2.__dict__,vars(p3)]
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('fazendo dump')
        dado = json.dump(bd, arquivo, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    print('Ele e o main')
    fazer_dump()