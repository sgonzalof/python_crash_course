# UF1291 - Despliegue (Python - Flask ejemplo básico)
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello from component!"

if __name__ == "__main__":
    app.run(port=5000)
