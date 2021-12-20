from flask import Flask
from flask import render_template

from Database.dbMysqlAlchemy import db_session, init_db
#from Database.users_db import form_user, form_login

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

@app.route('/categoria_altro.html')
def categoria_altro():  # put application's code here
    return render_template('categoria_altro.html')

@app.route('/categoria_auto.html')
def categoria_auto():  # put application's code here
    return render_template('categoria_auto.html')

@app.route('/categoria_console&videogiochi.html')
def categoria_console_e_videogiochi():  # put application's code here
    return render_template('categoria_console&videogiochi.html')

@app.route('/categoria_fotografia.html')
def categoria_fotografia():  # put application's code here
    return render_template('categoria_fotografia.html')

@app.route('/categoria_gioccatoli.html')
def categoria_giocattoli():  # put application's code here
    return render_template('categoria_gioccatoli.html')

@app.route('/categoria_informatica.html')
def categoria_informatica():  # put application's code here
    return render_template('categoria_informatica.html')

@app.route('/categoria_musica.html')
def categoria_musica():  # put application's code here
    return render_template('categoria_musica.html')

@app.route('/categoria_telefonia.html')
def categoria_telefonia():  # put application's code here
    return render_template('categoria_telefonia.html')

@app.route('/categoria_videomaker.html')
def categoria_videomaker():  # put application's code here
    return render_template('categoria_videomaker.html')


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
