from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "API funcionando!"


@app.route("/hello")
def hello():
    return "Olá, mundo!"


@app.route("/status")
def status():
    return {
        "status": "online",
        "message": "Aplicação funcionando corretamente"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


