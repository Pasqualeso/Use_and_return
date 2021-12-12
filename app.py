from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///mcdata.db'
db = SQLAlchemy(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/index.html')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/Utente.html')
def utente():  # put application's code here
    return render_template('utente.html')


@app.route('/Aggiungi Annuncio.html')
def aggiungi_annuncio():  # put application's code here
    return render_template('aggiungi Annuncio.html')


@app.route('/salva_annuncio')
def salva_annuncio():  # put application's code here
    return render_template('salva_annuncio.html')


@app.route('/Carrello.html')
def carrello():  # put application's code here
    return render_template('carrello.html')


@app.route('/categorie.html')
def categorie():  # put application's code here
    return render_template('categorie.html')


@app.route('/InformazioniUtente.html')
def informazioni_utente():  # put application's code here
    return render_template('informazioniUtente.html')


@app.route('/RegistrazioneUtente.html')
def registrazione_utente():  # put application's code here
    return render_template('registrazioneUtente.html')


@app.route('/PasswordDimenticata.html')
def password_dimenticata():  # put application's code here
    return render_template('passwordDimenticata.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
