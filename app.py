from flask import Flask, render_template, request, redirect
from model.comidas import mostrar_comidas_destaque
from model.comidas import mostrar_comidas_rapidas

# from model.comidas import inserir_comidas

app = Flask(__name__)


@app.route ("/")
def rapidos():
    itens_rapidos = mostrar_comidas_rapidas()
    itens_destaque = mostrar_comidas_destaque()
    return render_template("index.html", itens_rapidos=itens_rapidos, itens_destaque=itens_destaque)

# @app.route("/")
# def inserir():
#     produto = request.form.get("card__title")
#     descricao = request.form.get("card__description")
#     valor = request.form.get("card__price")
#     imagem = request.form.get("input-imagem")
 
#     inserir_comidas(produto, descricao, valor, imagem)
#     return redirect("/")


@app.route ("/site")
def site():
    return render_template("paginaSite.html")



if __name__ == "__main__":
    app.run(debug=True)