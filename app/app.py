from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index.html') # Define a rota para a página inicial
def home():
    # Retorna o template HTML chamado 'index.html'
    # Flask procura por este arquivo na pasta 'templates'
    return render_template('index.html')

    if __name__ == '__main__':
    app.run(debug=True)

