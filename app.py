from flask import Flask, render_template
from model.comidas import mostrar_comidas

app = Flask(__name__)

@app.route ("/")
def index():
    return render_template("index.html")

@app.route ("/site")
def site():
    return render_template("paginaSite.html")



if __name__ == "__main__":
    app.run(debug=True)