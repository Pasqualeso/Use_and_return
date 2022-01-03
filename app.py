import flask
from flask import Flask, render_template, session, request, url_for, flash, redirect
from flask_login import LoginManager
from flask_login._compat import unicode

from Database.annuncio_db import form_add_annuncio
from Database.dbMysqlAlchemy import db_session, init_db
from Database.utente_db import form_user, form_login_user, Utente, add_user, form_login_user
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    DateTimeField,
    RadioField,
    SelectField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import DataRequired

from Form.forms import LoginForm, RegistrationFormUtente, RegistrationFormAnnuncio, RegistrationFormRicerca

app = Flask(__name__)
db = init_db()
login_manager = LoginManager()
current_app_login = login_manager.init_app(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
curr_user = None


@app.route('/')
def index():  # put application's code here
    form_ricerca = RegistrationFormRicerca()

    if form_ricerca.validate_on_submit():
        session["oggetto_ricerca"] = form_ricerca.oggetto_ricerca
        session["categoria_ricerca"] = form_ricerca.categoria_ricerca
        session["regione_ricerca "] = form_ricerca.regione_ricerca
        session["data_inizio_noleggio_ricerca"] = form_ricerca.data_inizio_noleggio_ricerca
        session["data_fine_noleggio_ricerca"] = form_ricerca.data_fine_noleggio_ricerca

        submit_ricerca = form_ricerca.submit_ricerca

        form_ricerca.oggetto_ricerca = ""
        form_ricerca.categoria_ricerca = ""
        form_ricerca.regione_ricerca = ""
        form_ricerca.data_inizio_noleggio_ricerca = ""
        form_ricerca.data_fine_noleggio_ricerca = ""

    return render_template('index.html', form=form_ricerca)


@app.route('/index.html')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/registrazione_annuncio.html', methods=["GET", "POST"])
def registrazione_annuncio():  # put application's code here

    # Actions for the complicate form
    form_annuncio = RegistrationFormAnnuncio()

    # if the form is compiled
    if form_annuncio.validate_on_submit():
        id_utente = session["id_utente"]
        log_err = form_add_annuncio(db, form_annuncio, id_utente)
        return redirect(url_for("TEST_RISULTATO"))

    return render_template('registrazione_annuncio.html', form=form_annuncio)


@app.route('/salva_annuncio.html')
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


@app.route('/utente.html', methods=["GET", "POST"])
def utente():  # put application's code here

    form_log = LoginForm()

    if form_log.validate_on_submit():

        user = form_login_user(db, form_log)

        return redirect(url_for("TEST_RISULTATO"))

    return render_template('utente.html', form=form_log)


def get_id(self):
    return unicode(self.alternative_id)


@login_manager.user_loader
def load_user(user_id):
    return Utente.query.filter_by(alternative_id=user_id).first()


def logout():
    global curr_user
    curr_user = None
    session.pop('username_form')


'''
# localhost http://127.0.0.1:5000/<name>
@app.route('/informazioni_utente.html/<name>', methods=['GET', 'POST'])
def informazioni_utente(user):  # put application's code here

    return render_template('informazioni_utente.html')

'''

'''
@app.route('/informazioni_utente.html', methods=['GET', 'POST'])
def area_utente():
    return render_template('informazioni_utente.html')

'''

'''
@app.route('/registrazione_utente.html', methods=['GET', 'POST'])
def registrazione_utente():  # put application's code here
    log_err = form_user(db)
    if log_err is not None:
        print(log_err)
    return render_template('registrazione_utente.html', error=log_err)

'''


@app.route("/TEST_REGISTRAZIONE_UTENTE.html", methods=["GET", "POST"])
def super_form():
    # Actions for the complicate form
    form_utente = RegistrationFormUtente()

    if form_utente.validate_on_submit():
        log_err, nuovo_utente = form_user(db, form_utente)
        id_utente = session["id_utente"] = nuovo_utente.id_utente
        form_utente.id_utente = id_utente
        return redirect(url_for("TEST_RISULTATO"))

    return render_template("TEST_REGISTRAZIONE_UTENTE.html", form=form_utente)


@app.route("/TEST_RISULTATO.html", methods=["GET", "POST"])
def TEST_RISULTATO():
    flash("Form compilato con successo!")  # flash an alert message to the user
    return render_template("TEST_RISULTATO.html")


@app.route('/password_dimenticata.html')
def password_dimenticata():  # put application's code here
    return render_template('password_dimenticata.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
