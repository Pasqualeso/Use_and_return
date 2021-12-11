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
    return render_template('Utente.html')


@app.route('/Aggiungi Annuncio.html')
def aggiungi_annuncio():  # put application's code here
    return render_template('Aggiungi Annuncio.html')


@app.route('/salva_annuncio')
def salva_annuncio():  # put application's code here
    return render_template('salva_annuncio.html')


@app.route('/Carrello.html')
def carrello():  # put application's code here
    return render_template('Carrello.html')


@app.route('/Categorie.html')
def categorie():  # put application's code here
    return render_template('Categorie.html')


@app.route('/InformazioniUtente.html')
def informazioni_utente():  # put application's code here
    return render_template('InformazioniUtente.html')


@app.route('/RegistrazioneUtente.html')
def registrazione_utente():  # put application's code here
    return render_template('RegistrazioneUtente.html')


@app.route('/PasswordDimenticata.html')
def password_dimenticata():  # put application's code here
    return render_template('PasswordDimenticata.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
