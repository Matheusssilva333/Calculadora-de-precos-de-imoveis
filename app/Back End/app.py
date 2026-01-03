from flask import render_template, Flask

import requests

import python-dotenv

import numpy

import seaborn

import matplotlib

import pandas as pd


app = Flask(__name__)


@app.route('/index.html') # Define a rota para a página inicial
def home():
    # Retorna o template HTML chamado 'index.html'
    # Flask procura por este arquivo na pasta 'templates'
    return render_template('index.html')

    if __name__ == '__main__':
    app.run(debug=True)



