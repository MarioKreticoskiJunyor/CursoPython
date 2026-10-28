# CursoPython

Registro dos meus estudos de Python, feitos enquanto acompanho o curso
[Python 3 do zero ao avançado](https://www.udemy.com/course/python-3-do-zero-ao-avancado/) (Udemy).

Este repositório guarda a minha evolução: os arquivos são as anotações e os exercícios de
cada aula, do jeito que eu os escrevi enquanto aprendia. **Os estudos estão em andamento.**

## Objetivo

Construir uma base sólida em Python, da lógica de programação à orientação a objetos,
praticando cada conceito em código.

## Organização

| Pasta | Conteúdo | Arquivos |
|---|---|---|
| [`1_LogicadeProgramacao/`](1_LogicadeProgramacao) | Fundamentos da linguagem e lógica de programação | `aula1.py` a `aula67.py` |
| [`2_funcoes/`](2_funcoes) | Funções, estruturas de dados, módulos e programação funcional | `aula1.py` a `aula119*.py`, pacotes `aula99_package/` e `dados/` |
| [`AulaVenv/`](AulaVenv) | Ambientes virtuais, `pip` e `requirements.txt` | 2 arquivos |
| [`POO/`](POO) | Programação orientada a objetos | `aula120.py` a `aula140.py` |

Cada arquivo corresponde a uma aula ou a um exercício. Em alguns exercícios mantive
a minha tentativa e a solução apresentada no curso, para comparar as duas.

## Conhecimentos praticados

**Lógica de programação**
- Tipos de dados (`str`, `int`, `float`, `bool`), conversão de tipos e variáveis
- Entrada de dados, f-strings e formatação
- Condicionais (`if`/`elif`/`else`) e operadores lógicos e de pertinência (`in`, `not in`)
- Laços `while` e `for`, fatiamento de strings
- Listas, tuplas, `enumerate` e desempacotamento
- Uso do debugger
- Exercício de validação de CPF

**Funções e estruturas de dados**
- Definição de funções, escopo, `global`, `*args` e `**kwargs`
- Dicionários, sets e seus métodos
- `lambda`, list, dict e set comprehensions
- Valores truthy/falsy, tipos mutáveis e imutáveis, `isinstance`, `dir`, `hasattr`, `getattr`
- Iteráveis, iteradores, generators e `yield from`
- Tratamento de exceções (`try`/`except`/`else`/`finally`, `raise`)
- Módulos e pacotes próprios, módulos da biblioteca padrão
- Closures, `nonlocal`, decoradores e decoradores com parâmetros
- `itertools` (`count`, `combinations`, `permutations`, `product`, `groupby`), `map`, `filter`, `reduce`
- Recursividade
- Leitura e escrita de JSON
- Parâmetros mutáveis, parâmetros somente posicionais (`/`) e somente nomeados (`*`)
- Exercício de lista de tarefas com desfazer e refazer

**Ambientes virtuais**
- `venv`, `pip install`/`uninstall`, `pip freeze` e `requirements.txt`

**Orientação a objetos**
- Classes, instâncias, atributos e métodos
- Manutenção de estado dentro da classe
- Métodos de classe e factories
- `@property` e setters
- Associação, agregação e composição
- Herança múltipla

## Progresso

- Primeiro registro: agosto de 2023 · último registro: março de 2026
- Último tópico estudado: **herança múltipla** (`POO/aula140.py`)
- Próximo passo: continuar o módulo de orientação a objetos

## Como executar

Os arquivos são scripts independentes e usam apenas a biblioteca padrão.

```bash
python 1_LogicadeProgramacao/aula16.py
```

Alguns exercícios de `2_funcoes/` leem arquivos JSON por caminho relativo
(por exemplo, `2_funcoes\aula117.json`). Execute-os a partir da raiz do repositório.

## Observações

- Este é um repositório de estudos: o código não tem testes automatizados e não
  segue a organização de um projeto de produção.
- O `requirements.txt` da raiz foi gerado com `pip freeze` em uma das aulas de
  ambiente virtual e não é necessário para executar os exercícios.
