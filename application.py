from flask import Flask, redirect, url_for, request

app = Flask('framework_flask')


@app.route("/")
def ola():
    return u'Olá mundo! FLASK'

@app.route("/usuarios")
def index():
    return u'usuario logado'


#app.add_url_rule('/', endpoint='index', view_func='index')
@app.route("/usuarios/lista")
def lista_usuarios():
    return u'Uma lista de usuarios'


@app.route("/clientes/<function>")
def clientes(function):
    if function.lower() == "cadastro":
        return u"Pagina de cadastro"
    elif function.lower() == "lista":
        return u"?Lista de usuarios"


@app.route("/clientes/<int:id>")
def atualiza_cliente(id):
    return f"usuario {id}"

@app.route("/admin")
def ola_admin():
    return u"Ola admin"


@app.route("/visitante/<visitante>")
def ola_visitante(visitante):
    return f"Ola visitante {visitante}"


@app.route("/usuario/<nome>")
def ola_user(nome):
    if nome.lower() == "admin":
        return redirect(url_for('ola_admin'))
    elif nome.lower() == "visitante":
        return redirect(url_for('ola_visitante', visitante=nome))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return u"Executar login do usuario"
    elif request.method == 'GET':
        return u"Formulário de login"


if __name__ == "__main__":
    app.run()
