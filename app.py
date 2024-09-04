from flask import Flask, request, render_template
import csv
from datetime import datetime

app = Flask(__name__)

FILENAME = 'recursos.csv'

def inicializar_arquivo():
    try:
        with open(FILENAME, mode='r') as file:
            pass  # Arquivo já existe
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Quantidade', 'Data', 'Responsável', 'Tipo'])  # Cabeçalhos do CSV

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = request.form['quantidade']
        responsavel = request.form['responsavel']
        tipo = request.form['tipo']
        data = datetime.now().strftime('%d/%m/%Y')
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome, quantidade, data, responsavel, tipo])
        return 'Recurso registrado com sucesso!'
    return render_template('index.html')

if __name__ == '__main__':
    inicializar_arquivo()
    app.run(debug=True)
