from flask import Flask, render_template as rt, request, redirect, session, flash
from model.produtos import recuperar_produtos as rp, recuperar_produto_id as rpid, recuperar_produto_destaque as rpd
from model.usuario import inserir_usuario as iu, verificar_login as vl
from model.usuario import Usuario

app = Flask(__name__)
app.secret_key = "webservice_lanches"

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
    cadastro = Usuario(usuario, senha)
    if cadastro.cadastrar():
        return rt("login.html")
    else:
        flash("Este usuário já existe!", "erro")
        return redirect("/cadastro")

@app.route("/login")
def login():
    if "usuario_logado" in session:
        return redirect("/")
    return rt("login.html")

@app.route("/login/post", methods=["POST"])
def logar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    user = vl(usuario, senha)
    if user:
        session["usuario_logado"] = user
        return redirect("/")
    else:
        flash("Usuário ou senha inválidos!", "erro")
        flash("Tente novamente ou cadastre-se.", "erro")
        return redirect("/login")

@app.route("/lougout")
def lougout():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)