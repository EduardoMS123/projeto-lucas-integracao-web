#import do framework flask
#import do render_template para leitura html
#request para a captura dos dados
from flask import Flask, render_template, request
#biblioteca para criar a conexão com mysql
import mysql.connector as sqlconec

app = Flask(__name__)

bd_config = {
    'host': 'localhost',
    'user':'root',
    'password':'escola',
    'database': 'cadastro1'
}

#criação de rota para arquivo HTML principal
@app.route('/')
def index_route():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])




