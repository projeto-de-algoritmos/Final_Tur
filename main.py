from waitress import serve
from flask import Flask, render_template

import random
import itertools


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def pagina_principal():
    numeroNos = random.randint(3, 9)

    matrizDistancias = [[0] * numeroNos for i in range(numeroNos)]

    tabelaDistancias = []

    for i in range(numeroNos + 1):
        if not i:
            tabelaDistancias.append(
                ["Matriz de Distâncias"] +
                ["Local nº " + str(j + 1) for j in range(numeroNos)]
            )
        else:
            tabelaDistancias.append(["Local nº " + str(i)] + [0] * (numeroNos))

    for i in range(numeroNos):
        for j in range(i + 1, numeroNos):
            matrizDistancias[i][j] = \
                matrizDistancias[j][i] = random.randint(1, 99)

            tabelaDistancias[i + 1][j + 1] = \
                tabelaDistancias[j + 1][i + 1] = matrizDistancias[i][j]

    quantidadeNos = len(matrizDistancias)

    objetosSubgrafos = []
    for tamanhoSubGrafos in range(2, quantidadeNos):
        # Gerar subgrafos com, no mínimo, 2 nós e,
        # no máximo, o número de nós do grafo base menos 1
        objetosSubgrafos.append(
            itertools.combinations(
                range(1, quantidadeNos), tamanhoSubGrafos
            )
        )

        # Obs.: O primeiro nó sempre é o local de início do percurso,
        # por isso não é incluso nessa geração de subgrafos

        # Os subgrafos do primeiro nó são definidos no código javascript

    conjuntosSubgrafos = []
    for conjuntoSubgrafos in objetosSubgrafos:
        subgrafos = []

        for subgrafo in conjuntoSubgrafos:
            subgrafo = list(subgrafo)
            subgrafos.append(subgrafo)

        conjuntosSubgrafos.append(subgrafos)

    return render_template(
        "pagina_principal.html",
        matrizDistancias=matrizDistancias,
        conjuntosSubgrafos=conjuntosSubgrafos,
        tabelaDistancias=tabelaDistancias
    )


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
