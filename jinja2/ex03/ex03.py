from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/ola")
def ola_mundo():
    usuario = request.args.get('usuario', 'evaldo')
    return render_template('index.html', usuario=usuario)


if __name__ == '__main__':
    app.run(debug=True)