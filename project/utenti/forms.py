from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from project.utenti.models import Utente

'''
Tutti i messaggi sono stati personalizzati in italiano
Tolta la validazione standard nella form
'''


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email obbligatoria'), Length(1, 64),
                                             Email(message="Email non valida")])
    password = PasswordField('Password', validators=[DataRequired(message='Password obbligatoria')])
    remember_me = BooleanField('Ricordami su questo sito')
    submit = SubmitField('Entra')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email obbligatoria'), Length(1, 64),
                                             Email(message="Email non valida")])
    username = StringField('Username', validators=[
        DataRequired(message='Username obbligatorio'), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Nome utente deve essere composto solo da lettere, numeri, punti o underscores')])

    password = PasswordField('Password', validators=[
        DataRequired(message='Password obbligatoria'),
        EqualTo('password2', message='Le due password devono combaciare')])
    password2 = PasswordField('Conferma password', validators=[DataRequired(message='Conferma password obbligatoria')])
    nome_utente = StringField("Inserisci il tuo nome", validators=[DataRequired(), Length(1, 64)])
    cognome_utente = StringField("Inserisci il tuo cognome", validators=[DataRequired(), Length(1, 64)])
    sesso = SelectField(
        "Inserisci il tuo sesso: ",
        choices=[("uomo", "UOMO"), ("donna", "DONNA"), ("indefinito", "INDEFINITO")], validators=[DataRequired()]
    )
    citta = StringField('Inserisci la città', validators=[DataRequired(message='Città obbligatoria'), Length(1, 64)])
    telefono = StringField("Inserisci il tuo numero di telefono", validators=[DataRequired()])
    data_di_nascita = DateField("Inserisci la data di nascita", format='%Y-%m-%d', validators=[DataRequired()])
    provincia = SelectField(
        "Inserisci la provincia",
        choices=[("ag", "Agrigento"), ("al", "Alessandria"), ("an", "Ancona"), ("ao", "Aosta"), ("ar", "Arezzo"),
                 ("ap", "Ascoli Piceno"),
                 ("at", "Asti"), ("av", "Avellino"), ("ba", "Bari"), ("bt", "Barletta-Andria-Trani"), ("bl", "Belluno"),
                 ("bn", "Benevento"),
                 ("bg", "Bergamo"), ("bi", "Biella"), ("bo", "Bologna"), ("bz", "Bolzano"), ("bs", "Brescia"),
                 ("br", "Brindisi"), ("ca", "Cagliari"),
                 ("cl", "Caltanissetta"), ("cb", "Campobasso"), ("ci", "Carbonia - iglesias "), ("ce", "Caserta"),
                 ("ct", "Catania"), ("cz", "Catanzaro"),
                 ("ch", "Chieti"), ("co", "Como"), ("cs", "Cosenza"), ("cr", "Cremona"), ("kr", "Crotone"),
                 ("cn", "Cuneo"), ("en", "Enna"), ("fm", "Fermo"),
                 ("fe", "Ferrara"), ("fi", "Firenze"), ("fg", "Foggia"), ("fc", "Forli-Cesena"), ("fr", "Frosinone"),
                 ("ge", "Genova"), ("go", "Gorizia"),
                 ("gr", "Grosseto"), ("im", "Imperia"), ("is", "Isernia"), ("sp", "La spezia"), ("aq", "L'aquila"),
                 ("lt", "Latina"), ("le", "Lecce"),
                 ("lc", "Lecco"), ("li", "Livorno"), ("lo", "Lodi"), ("lu", "Lucca"), ("mc", "Macerata"),
                 ("mn", "Mantova"), ("ms", "Massa - Carrara"),
                 ("mt", "Matera"), ("vs", "Medio Campidano"), ("me", "Messina"), ("mi", "Milano"), ("mo", "Modena"),
                 ("mb", "Monza e della Brianza"),
                 ("na", "Napoli"), ("no", "Novara"), ("nu", "Nuoro"), ("og", "Ogliastra"), ("ot", "Olbia - Tempio"),
                 ("or", "Oristano"), ("pd", "Padova"),
                 ("pa", "Palermo"), ("pr", "Parma"), ("pv", "Pavia"), ("pg", "Perugia"), ("pu", "Pesaro e Urbino"),
                 ("pe", "Pescara"), ("pc", "Piacenza"),
                 ("pi", "Pisa"), ("pt", "Pistoia"), ("pn", "Pordenone"), ("pz", "Potenza"), ("po", "Prato"),
                 ("rg", "Ragusa"), ("ra", "Ravenna"), ("rc", "Reggio di Calabria"),
                 ("re", "Reggio nell'Emilia"), ("ri", "Rieti"), ("rn", "Rimini"), ("rm", "Roma"), ("ro", "Rovigo"),
                 ("sa", "Salerno"), ("ss", "Sassari"),
                 ("sv", "Savona"), ("si", "Siena"), ("sr", "Siracusa"), ("so", "Sondrio"), ("ta", "Taranto"),
                 ("te", "Teramo"), ("tr", "Terni"), ("to", "Torino"),
                 ("tp", "Trapani"), ("tn", "Trento"), ("tv", "Treviso"), ("ts", "Trieste"), ("ud", "Udine"),
                 ("va", "Varese"), ("ve", "Venezia"), ("vb", "Verbano - Cusio - Ossola "),
                 ("vc", "Vercelli"), ("vr", "Verona"), ("vv", "ibo valentia"), ("vi", "Vicenza"), ("vt", "Viterbo")]
        , validators=[DataRequired()])
    via = StringField("Inserisci la via", validators=[DataRequired()])
    cap = StringField("Inserisci il cap", validators=[DataRequired()])

    submit = SubmitField('Registrati')

    def validate_email(self, field):
        if Utente.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(u'Email già registrata.')

    def validate_username(self, field):
        if Utente.query.filter_by(username=field.data).first():
            raise ValidationError(u'Username già in uso.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Vecchia password', validators=[DataRequired(message='Vecchia password obbligatoria')])
    password = PasswordField('Nuova password', validators=[
        DataRequired(message='Nuova password obbligatoria'),
        EqualTo('password2', message='Le due passwords devono essere uguali')])
    password2 = PasswordField('Conferma nuova password',
                              validators=[DataRequired(message='Conferma nuova password obbligatoria')])
    submit = SubmitField('Aggiorna password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email obbligatoria'), Length(1, 64),
                                             Email(message="Email non valida")])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Nuova password', validators=[
        DataRequired(message='Nuova password obbligatoria'),
        EqualTo('password2', message='Le due passwords devono essere uguali')])
    password2 = PasswordField('Conferma password',
                              validators=[DataRequired(message='Conferma nuova password obbligatoria')])
    submit = SubmitField('Reset Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('Nuova Email', validators=[DataRequired(message='Nuova email obbligatoria'), Length(1, 64),
                                                   Email(message="Email non valida")])
    password = PasswordField('Password', validators=[DataRequired(message='Password obbligatoria')])
    submit = SubmitField('Email aggiornata')

    def validate_email(self, field):
        if Utente.query.filter_by(email=field.data.lower()).first():
            raise ValidationError(u'Email già registrata.')
