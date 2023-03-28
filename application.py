from flask import Flask

app = Flask(__name__)


@app.route("/")
def ola():
    return u'Olá mundo! FLASK'


if __name__ == "__main__":
    app.run()
