import datetime
import uuid
import smtplib
from datetime import date

from flask import request
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import exc
from sqlalchemy.orm import mapper
from sqlalchemy.sql.functions import now

from Database.dbMysqlAlchemy import db_session, metadata


# CLASSE UTENTE
class Utente(object):
    query = db_session.query_property()
    __tablename__ = 'Utente'
    id_utente = Column(String(12), primary_key=True)
    nome_utente = Column(String(50), nullable=False)
    cognome_utente = Column(String(50), nullable=False)
    email_utente = Column(String(120), nullable=False)
    username_utente = Column(String(50), nullable=False, unique=True)
    password_utente = Column(String(50), nullable=False)
    sesso_utente = Column(String(1), nullable=False)
    data_di_nascita_utente = Column(String(30), nullable=False)
    telefono_utente = Column(String(20), nullable=False)
    citta_utente = Column(String(50), nullable=False)
    provincia_utente = Column(String(50), nullable=False)
    via_utente = Column(String(120), nullable=False)
    cap_utente = Column(Integer, nullable=False)
    data_creazione_utente = Column(String(30), nullable=False)

    # COSTRUTTORE CREAZIONE UTENTE
    def __init__(self, nome, cognome, email, username, password, sesso, data_di_nascita, telefono, citta,provincia, via, cap):
        self.id_utente = self.generate_id(username)
        self.nome_utente = nome
        self.cognome_utente = cognome
        self.email_utente = email
        self.username_utente = username
        self.password_utente = password
        self.sesso_utente = sesso
        self.data_di_nascita_utente = data_di_nascita
        self.telefono_utente = telefono
        self.citta_utente = citta
        self.provincia_utente = provincia
        self.via_utente = via
        self.cap_utente = cap
        self.data_creazione_utente = datetime.datetime.now()

    # COSTRUTTORE CARICA UTENTE
    '''
    def __init__(self, id, nome, cognome, email, username, password, sesso, data_di_nascita, telefono, citta,provincia, via, cap,data_creazione):
        self.id_utente = id
        self.nome_utente = nome
        self.cognome_utente = cognome
        self.email_utente = email
        self.username_utente = username
        self.password_utente = password
        self.sesso_utente = sesso
        self.data_di_nascita_utente = data_di_nascita
        self.telefono_utente = telefono
        self.citta_utente = citta
        self.provincia_utente = provincia
        self.via_utente = via
        self.cap_utente = cap
        self.data_creazione_utente = data_creazione
    '''
    # FUNZIONE STAMPA UTENTE
    def __repr__(self):
        return f'<Utente {self.id_utente + self.nome_utente + self.cognome_utente + self.email_utente + self.username_utente + self.password_utente + self.sesso_utente + self.data_di_nascita_utente + self.citta_utente + self.provincia_utente + self.via_utente + self.cap_utente + self.data_creazione_utente!r}> '

    # FUNZIONE GENERA ID IN BASE ALL'USERNAME E AD UN ID CASUALE
    def generate_id(self, username):
        id_seed = uuid.uuid4()
        string_temp = username
        uid = uuid.uuid3(id_seed, string_temp)
        uuid_final = str(uid)[:13].replace("-", "")

        print(uuid_final)
        return uuid_final


# Mappatura della classe utente per la gestione nel database
utenti = Table('utente', metadata,
               Column('id_utente', String(12), primary_key=True),
               Column('nome_utente', String(50), nullable=False),
               Column('cognome_utente', String(50), nullable=False),
               Column('username_utente', String(50), nullable=False),
               Column('email_utente', String(120), nullable=False),
               Column('username_utente', String(50), nullable=False, unique=True),
               Column('password_utente', String(50), nullable=False),
               Column('sesso_utente', String(1), nullable=False),
               Column('data_di_nascita_utente', String(30), nullable=False),
               Column('telefono_utente', String(20), nullable=False),
               Column('citta_utente', String(50), nullable=False),
               Column('provincia_utente', String(50), nullable=False),
               Column('via_utente', String(120), nullable=False),
               Column('cap_utente', Integer, nullable=False),
               Column('data_creazione_utente', String(30), nullable=False)
               )
mapper(Utente, utenti)


# CLASSE PER LA GESTIONE DELLE ECCEZIONI DEGLI UTENTI
class UserException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


'''
def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail\n")
'''


# Metodo per leggere i campi dai vari form di registrazione per creare un nuovo utente
def form_user(db):

    if request.method == 'POST':
        nome = request.form.get('nome')
        cognome = request.form.get('cognome')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        sesso = request.form.get('sesso')
        data_nascita_utente = request.form.get('data_nascita_utente')
        telefono = request.form.get('telefono')
        citta = request.form.get('citta')
        provincia = request.form.get('provincia')
        via = request.form.get('via')
        cap = request.form.get('cap')

        nuovo_utente = Utente(nome, cognome, email, username, password, sesso, data_nascita_utente, telefono, citta, provincia, via, cap)

        log_err = add_user(db, nuovo_utente)

        return log_err


# Metodo per aggiungere un nuovo utente al database
def add_user(db, utente_inserito):
    try:
        db.connect()
        nuovo_utente = utente_inserito
        if nuovo_utente is None:
            raise UserException("Utente non valido\n")
        else:
            # Aggiunge un nuovo utente nel database
            db_session.add(nuovo_utente)
            db_session.commit()
    except exc.SQLAlchemyError as ex:
        print(ex.__doc__)
        return ex

    return None


# Metodo per leggere i campi dai vari form di login per effettuare la query di controllo
def form_login(db):
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']

        query_login = "SELECT * FROM utenti WHERE Username = %s AND Password = %s"
        valori_query = (username_form, password_form)
        utente = control_user(db, query_login, valori_query)
        if utente is None:
            return None
        return utente


# Metodo per effettuare una query di controllo sugli Username e password inseriti per accedere all'account
def control_user(db, query_login, valori_query):
    try:
        cursor = db.connect()
        result = cursor.execute(query_login, valori_query)
        utente = result.fetchone()
        db_session.commit()
    except exc.SQLAlchemyError as ex:
        print(ex.__doc__)
        return None

    return utente
