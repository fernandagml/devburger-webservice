from flask import Flask, render_template as rt
from model.produtos import recuperar_produtos as rp, recuperar_produto_id as rpid, recuperar_produto_destaque as rpd

app = Flask(__name__)

@app.route("/")
def index():
    produtos = rp()
    destaques = rpd()
    return rt("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<id>")
def hamburguer(id):
    produto = rpid(id)
    return rt("/produto.html", produto = produto)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)