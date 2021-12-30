import flask
from flask import Flask, render_template, session, request, url_for, flash, redirect
from flask_login import LoginManager
from flask_login._compat import unicode
from Database.dbMysqlAlchemy import db_session, init_db
from Database.utente_db import form_user, form_login, Utente
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

from Form.forms import LoginForm, RegistrationFormUtente, RegistrationFormAnnuncio

app = Flask(__name__)
db = init_db()
login_manager = LoginManager()
current_app_login = login_manager.init_app(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
curr_user = None


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/index.html')
def home():  # put application's code here
    return render_template('index.html')


@app.route('/registrazione_annuncio.html')
def registrazione_annuncio():  # put application's code here

    # Actions for the complicate form
    form_annuncio = RegistrationFormAnnuncio

    # if the form is compiled
    if form_annuncio.validate_on_submit():
        # save form information into session user cookie
        session["titolo"] = form_annuncio.titolo.data
        session["categoria"] = form_annuncio.categoria.data
        session["descrizione"] = form_annuncio.descrizione.data
        session["data_inizio_noleggio"] = form_annuncio.data_inizio_noleggio.data
        session["data_fine_noleggio"] = form_annuncio.data_fine_noleggio.data
        session["immagine"] = form_annuncio.immagine.data

        submit = SubmitField("Submit")

        # reset the form
        form_annuncio.titolo.data = ""
        form_annuncio.categoria.data = ""
        form_annuncio.descrizione.data = ""
        form_annuncio.data_inizio_noleggio.data = ""
        form_annuncio.data_fine_noleggio.data = ""

        # go to the thankyou template page (thankyou function in python file)
        return redirect(url_for("salva_annuncio"))

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
# Login Utente
@app.route('/utente.html', methods=['GET', 'POST'])
def utente():  # put application's code here
    global curr_user
    formLog = LoginForm()
    user = form_login(db,formLog)

    formLog.username.data = ""  # reset
    formLog.password.data = ""  # reset

    # print(curr_user.__repr__())

    return redirect(flask.url_for('informazioni_utente', user=curr_user, form=formLog))
    # return f'Logged in as {session["username_form"]}'

    return render_template('utente.html', form=formLog)
'''

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

    # if the form is compiled
    if form_utente.validate_on_submit():
        # save form information into session user cookie
        session["nome_utente"] = form_utente.nome_utente.data
        session["cognome_utente"] = form_utente.cognome_utente.data
        session["email"] = form_utente.email.data
        session["username"] = form_utente.username.data
        session["password"] = form_utente.password.data
        session["sesso"] = form_utente.sesso.data
        session["telefono"] = form_utente.telefono.data
        session["data_di_nascita"] = form_utente.data_di_nascita.data
        session["citta"] = form_utente.citta.data
        session["provincia"] = form_utente.provincia.data
        session["via"] = form_utente.via.data
        session["cap"] = form_utente.cap.data

        submit = SubmitField("Submit")
        # reset the form
        form_utente.nome_utente.data = ""
        form_utente.cognome_utente.data = ""
        form_utente.email.data = ""
        form_utente.username.data = ""
        form_utente.password.data = ""
        form_utente.sesso.data = ""
        form_utente.data_di_nascita.data = ""
        form_utente.citta.data = ""
        form_utente.provincia.data = ""
        form_utente.via.data = ""
        form_utente.cap.data = ""

        # go to the thankyou template page (thankyou function in python file)
        return redirect(url_for("TEST_RISULTATO"))

    return render_template("TEST_REGISTRAZIONE_UTENTE.html", form=form_utente)


@app.route("/TEST_RISULTATO.html", methods=["GET", "POST"])
def TEST_RISULTATO():
    flash("Form compiled succesfully!")  # flash an alert message to the user
    return render_template("TEST_RISULTATO.html")


@app.route('/password_dimenticata.html')
def password_dimenticata():  # put application's code here
    return render_template('password_dimenticata.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
