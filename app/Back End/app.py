from flask import render_template, Flask

import requests

import python-dotenv

import numpy as np

import seaborn

import matplotlib

import pandas as pd

import tkinter as tk


app = Flask(__name__)

# Rota da página inicial

@app.route('/') 
def home(): return "Seja bem vindo!"
print ("Clique aqui")

# Rota Página de pesquisa de preços
@app.route('/index.html')
def Cálculo_de_preços () : return "index.html"


    if __name__ == '__main__':
    app.run(debug=True)



