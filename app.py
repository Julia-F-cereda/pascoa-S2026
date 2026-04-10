from flask import Flask, render_template, request, redirect
from model.comidas import mostrar_comidas_destaque
from model.comidas import mostrar_comidas_rapidas
from model.comidas import mostrar_produto

# from model.comidas import inserir_comidas

app = Flask(__name__)


@app.route ("/")
def rapidos():
    itens_rapidos = mostrar_comidas_rapidas() #morreu aquui
    itens_destaque = mostrar_comidas_destaque() #morreu aqui
    return render_template("index.html", itens_rapidos=itens_rapidos, itens_destaque=itens_destaque) #morreu aqui

# @app.route("/")
# def inserir():
#     produto = request.form.get("card__title")
#     descricao = request.form.get("card__description")
#     valor = request.form.get("card__price")
#     imagem = request.form.get("input-imagem")
 
#     inserir_comidas(produto, descricao, valor, imagem)
#     return redirect("/")


@app.route ("/produto/<codigo>")
def site(codigo):
    produto = mostrar_produto(codigo)
    return render_template("produto.html", produto=produto)



if __name__ == "__main__":
    app.run(debug=True)