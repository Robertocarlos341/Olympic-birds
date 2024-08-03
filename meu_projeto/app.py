from flask import Flask, request, render_template

app = Flask(__name__)

# Lista de itens para simular a pesquisa
itens = [
    "Astronomia",
    "Quem Somos",
    "Contato",
    "Alguma Coisa",
    "Departamento",
    "Física",
    "Gabaritos Física",
    "index",
    "Línguistica",
    "Problemas da semana"
    "semana"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    termo_pesquisa = request.form['pesquisa'].lower()
    resultados = [item for item in itens if termo_pesquisa in item.lower()]
    return render_template('resultado.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)