from waitress import serve
from flask import Flask, render_template

import itertools


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def pagina_principal():
    matrizDistancias = [[0, 1, 23, 95, 61], [1, 0, 23, 18, 13], [23, 23, 0, 55, 52], [95, 18, 55, 0, 45], [61, 13, 52, 45, 0]]

    quantidadeDistancias = len(matrizDistancias)

    objetosSubgrafos = []
    for tamanhoSubGrafos in range(2, quantidadeDistancias):
        # Gerar subgrafos
        objetosSubgrafos.append(
            itertools.combinations(
                range(1, quantidadeDistancias), tamanhoSubGrafos
            )
        )

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
