from waitress import serve
from flask import Flask, render_template

import itertools


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def pagina_principal():
    matrizDistancias = [
        [0, 95, 5, 36, 51],
        [95, 0, 95, 85, 70],
        [5, 95, 0, 90, 70],
        [36, 85, 90, 0, 88],
        [51, 70, 70, 88, 0]
    ]

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
        conjuntosSubgrafos=conjuntosSubgrafos
    )


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
