from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# utilizando sistema de templates string jinja 2
# função que apresenta pagina de boas vindas
@app.route('/usuarios/<user_name>')
def sucess(user_name):
    return render_template('index.html', user_name=user_name, title="Pagina boas vindas")


# função que faz login no sistema
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        return redirect(url_for('sucess', user_name=user_name))
    else:
        user_name = request.args.get('user_name')
        return redirect(url_for('sucess', user_name=user_name))


if __name__ == '__main__':
    app.run(debug=True)