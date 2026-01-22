from flask import render_template, Flask

import requests

import python-dotenv

import numpy as np

import seaborn

import matplotlib

import pandas as pd


app = Flask(__name__)

# Rota da página inicial

@app.route('/') 

return render_template('/index.html')

print ("Clique aqui")

if __name__ == '__main__':
    app.run(debug=True)



