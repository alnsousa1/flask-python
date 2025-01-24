from flask import Flask, url_for, render_template

# iniciando o flask
app = Flask(__name__)

# rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de usuários"
    usuarios = [
        {"nome": "Allan", "membro_ativo":True},
        {"nome": "Cauã", "membro_ativo":False},
        {"nome": "Giovana", "membro_ativo":False}
    ]
    #primeiro parametro é a variavel de contexto, ou seja, a variavel que será enviada para o front-end, no caso, context_titulo e context_usuarios
    return render_template('index.html', context_titulo=titulo, context_usuarios=usuarios)


@app.route("/pagina_sobre")
def pagina_sobre():
    return "teste sobre"

# execucao
app.run(debug=True)   