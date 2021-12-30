from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField, \
    EmailField, DateField, IntegerField, FileField
from wtforms.validators import InputRequired, EqualTo, DataRequired


class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("submit")


################################################
class RegistrationFormUtente(FlaskForm):
    nome_utente = StringField("Inserisci il tuo nome", validators=[DataRequired()])
    cognome_utente = StringField("Inserisci il tuo cognome", validators=[DataRequired()])
    email = EmailField("Inserisci la tua email", validators=[DataRequired()])
    username = StringField("Inserisci il tuo username", validators=[DataRequired()])
    password = PasswordField("Inserisci la tua password", validators=[DataRequired()])
    sesso = SelectField(
        "Inserisci il tuo sesso: ",
        choices=[("m", "M"), ("f", "F"), ("n", "N")]
        , validators=[DataRequired()]
    )
    telefono = StringField("Inserisci il tuo numero di telefono", validators=[DataRequired()])
    data_di_nascita = DateField("Inserisci la data di nascita", format='%Y-%m-%d', validators=[DataRequired()])
    citta = StringField("Inserisci la citta", validators=[DataRequired()])
    provincia = StringField("Inserisci la provincia", validators=[DataRequired()])
    via = StringField("Inserisci la via", validators=[DataRequired()])
    cap = IntegerField("Inserisci il cap", validators=[DataRequired()])

    submit = SubmitField("Submit")


class RegistrationFormAnnuncio(FlaskForm):
    titolo = StringField("Inserisci il titolo della categoria", validators=[DataRequired()])
    categoria = StringField("Inserisci la categoria", validators=[DataRequired()])
    descrizione = StringField("Inserisci una descrizione(Max 200 caratteri)", validators=[DataRequired()])
    data_inizio_noleggio = DateField("Inserisci una data di inizio noleggio", validators=[DataRequired()])
    data_fine_noleggio = DateField("Inserisci una data di fine noleggio", validators=[DataRequired()])
    immagine = FileField("Inserisci un'immagine", validators=[DataRequired()])

    submit = SubmitField("Submit")