from flask import Flask

app = Flask(_name_)

@app.router('/')
def hello():
    return("Bem-vindo à API de análise de casos criminais")

if__name__='__main__'
    app.run(debug=True) 