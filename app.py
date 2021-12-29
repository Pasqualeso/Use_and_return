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

from Form.forms import LoginForm, RegistrationFormUtente

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
    course_form = RegistrationFormUtente()

    # if the form is compiled
    if course_form.validate_on_submit():
        # save form information into session user cookie
        session["course_name"] = course_form.course_name.data
        session["course_active"] = course_form.course_active.data
        session["difficulty"] = course_form.difficulty.data
        session["platform"] = course_form.platform.data
        session["note"] = course_form.note.data

        # reset the form
        course_form.course_name.data = ""
        course_form.course_active.data = ""
        course_form.difficulty.data = ""
        course_form.platform.data = ""
        course_form.note.data = ""

        # go to the thankyou template page (thankyou function in python file)
        return redirect(url_for("TEST_RISULTATO"))

    return render_template("TEST_REGISTRAZIONE_UTENTE.html", form=course_form)


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
