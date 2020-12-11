# Tur

**Número da Lista**: 6<br>
**Conteúdo da Disciplina**: Final<br>

## Alunos
| Matrícula | Aluno |
| -- | -- |
| 17/0013812 | [Matheus Rodrigues](https://github.com/rjoao) |

## Sobre
O objetivo do projeto é possibilitar a visualização da aplicação do algoritmo Held-Karp em um grafo para encontrar o percurso que:
 - Visite todos os vértices do grafo;
 - Retorne ao ponto inicial, vértice inicial;
 - Possua o menor custo.

O algoritmo é aplicado sobre o grafo representado na tela de maneira convencional. O número de nós do grafo e os custos de deslocamento entre eles são gerados aleatoriamente a cada execução do projeto. Mas essa característica pode ser alterada no código fonte e os valores serem definidos manualmente.

Os seguintes passos estão presentes no projeto:
 - Geração do grafo
 - Definição da velocidade normal de execução do algoritmo.
 - Construção do grafo
  - Identificação de subgrafos
    - Visualização em etapas
 - Análise de deslocamentos
    - Visualização em etapas
 - Identificação de melhor percurso
    - Visualização em etapas
 - Apresentação do melhor percurso
    - Visualização em etapas


## Screenshots

### Página Inicial
![Página Inicial](./static/media/s_pagina_inicial.png)

### Execução Algoritmo

#### Deslocamentos Nó Inicial
![Deslocamento Inicial](./static/media/s_exec_deslocamento_inicial.png)

#### Subgrafos
![Subgrafos](./static/media/s_exec_subgrafo.png)

#### Deslocamentos Subgrafos
![Deslocamentos Subgrafos](./static/media/s_exec_deslocamento_subgrafo.png)

#### Percurso Menor Custo - Identificação
![Identificação Percurso](./static/media/s_exec_identificacao_percurso.png)

#### Percurso Menor Custo - Construção
![Construção Percurso](./static/media/s_exec_construcao_percurso.png)

#### Percurso Menor Custo
![Percurso Menor Custo](./static/media/s_exec_percurso_menor_custo.png)


## Instalação 
**Linguagem**: Python3<br>

É necessário possuir o sistema de gerenciamento de pacotes **pip3**.

Se não possuir, no Ubuntu, rode o seguinte comando no terminal:

```
sudo apt-get install python3-pip
```

## Uso 

No terminal, primeiro instale os requisitos do projeto e depois execute o arquivo principal.

### Instalação dos requisitos

```
make install
```

### Execução do projeto

```
make run
```
