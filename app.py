from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
def home():
    return "Home"

@app.route("/hello")
def hello():
    return "Hello Word"

@app.route("/meu-contato")
def meuContato():
    return render_template('meucontato.html')

