from flask import render_template, Flask

import requests

import python-dotenv

import numpy as np

import seaborn

import matplotlib

import pandas as pd


app = Flask(__name__)


@app.route('/') 
def home():
    
    return render_template('index.html')

    if __name__ == '__main__':
    app.run(debug=True)



