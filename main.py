from waitress import serve
from flask import Flask, render_template

import itertools


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def pagina_principal():
    matrizDistancias = [
        [0, 83, 54, 61, 61], [83, 0, 99, 38, 90], [54, 99, 0, 60, 14],
        [61, 38, 60, 0, 56], [61, 90, 14, 56, 0]
    ]

    quantidadeDistancias = len(matrizDistancias)

    objetosCombinacoes = []
    for i in range(2, quantidadeDistancias):
        objetosCombinacoes.append(
            itertools.combinations(range(1, quantidadeDistancias), i)
        )

    combinacoesTotais = []
    for objetoCombinacoes in objetosCombinacoes:
        combinacoes = []

        for combinacao in objetoCombinacoes:
            combinacao = list(combinacao)
            combinacoes.append(combinacao)

        combinacoesTotais.append(combinacoes)

    return render_template(
        "pagina_principal.html",
        matrizDistancias=matrizDistancias,
        combinacoes=combinacoesTotais
    )


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
