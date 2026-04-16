from flask import Flask, render_template as rt, request, redirect
from model.produtos import recuperar_produtos as rp, recuperar_produto_id as rpid, recuperar_produto_destaque as rpd
from model.usuario import inserir_usuario as iu, verificar_login as vl

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

@app.route("/cadastro")
def cadastro():
    return rt("cadastro.html")

@app.route("/cadastro/post", methods=["POST"])
def cadastrar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    iu(usuario, senha)
    return rt("login.html")

@app.route("/login")
def login():
    return rt("login.html")

@app.route("/login/post", methods=["POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    user = vl(usuario, senha)
    if user:
        # session["usuario_logado"] = user
        # flash("Login realizado com sucesso. Seja bem-vindo(a) {usuario}!", "sucesso")
        return redirect("/")
    else:
        # flash("Usuário ou senha inválidos!", "erro")
        # flash("Tente novamente ou cadastre-se para acessar a área de administração.", "erro")
        return redirect("/login")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)