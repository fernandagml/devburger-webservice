from flask import Flask, render_template as rt
from model.produtos import recuperar_produtos as rp

app = Flask(__name__)

@app.route("/")
def index():
    produtos = rp(1)
    return rt("index.html", produtos = produtos)

@app.route("/hamburguer")
def hamburguer():
    return rt("/destaques.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)