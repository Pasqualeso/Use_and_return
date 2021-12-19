from flask import Flask
from flask import render_template

from Database.dbMysqlAlchemy import db_session, init_db
from Database.users_db import form_user, form_login

app = Flask(__name__)
db = init_db()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/index.html')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/utente.html')
def utente():  # put application's code here
    return render_template('utente.html')


@app.route('/registrazione_annuncio.html')
def registrazione_annuncio():  # put application's code here
    return render_template('registrazione_annuncio.html')


@app.route('/salva_annuncio')
def salva_annuncio():  # put application's code here
    return render_template('salva_annuncio.html')


@app.route('/carrello.html')
def carrello():  # put application's code here
    return render_template('carrello.html')


@app.route('/categorie.html')
def categorie():  # put application's code here
    return render_template('categorie.html')


@app.route('/informazioni_utente.html')
def informazioni_utente():  # put application's code here
    return render_template('informazioni_utente.html')


@app.route('/registrazione_utente.html')
def registrazione_utente():  # put application's code here
    return render_template('registrazione_utente.html')


@app.route('/password_dimenticata.html')
def password_dimenticata():  # put application's code here
    return render_template('password_dimenticata.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
