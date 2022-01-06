from flask import session, redirect, url_for
from sqlalchemy import String, Column, Integer, Table, exc
from sqlalchemy.orm import mapper

from Database.dbMysqlAlchemy import db_session, metadata


class Annuncio(object):
    query = db_session.query_property()
    __tablename__ = 'Annuncio'
    id_annuncio = Column(String(12), primary_key=True)
    titolo_annuncio = Column(String(50), nullable=False)
    categoria_annuncio = Column(String(50), nullable=False)
    prezzo_per_giorno_annuncio = Column(Integer, nullable=False)
    descrizione_annuncio = Column(String(200), nullable=False)
    data_inizio_noleggio = Column(String(30), nullable=False)
    data_fine_noleggio = Column(String(30), nullable=False)
    data_inserimento_annuncio = Column(String(30), nullable=False)
    disponibile = Column(Integer, nullable=False)
    id_utente_rf_annuncio = Column(String(12), nullable=False)

    # COSTRUTTORE CREAZIONE ANNUNCIO
    def __init__(self, id_annuncio, titolo, categoria, prezzo, descrizione, data_inizio, data_fine, data_inserimento,
                 disponibilita,
                 id_utente):
        self.id_annuncio = id_annuncio
        self.titolo_annuncio = titolo
        self.categoria_annuncio = categoria
        self.prezzo_per_giorno_annuncio = prezzo
        self.descrizione_annuncio = descrizione
        self.data_inizio_noleggio = data_inizio
        self.data_fine_noleggio = data_fine
        self.data_inserimento_annuncio = data_inserimento
        self.disponibile = disponibilita
        self.id_utente_rf_annuncio = id_utente

    # FUNZIONE STAMPA ANNUNCIO
    def __repr__(self):
        return f'<Annuncio {self.id_annuncio + self.titolo_annuncio + self.categoria_annuncio + self.prezzo_per_giorno_annuncio + self.descrizione_annuncio + self.data_inizio_noleggio + self.data_fine_noleggio + self.data_inserimento_annuncio + self.disponibile + self.id_utente_rf_annuncio!r}> '


# Mappatura della classe utente per la gestione nel database
annunci = Table('annuncio', metadata,
                Column('id_annuncio', String(12), primary_key=True),
                Column('titolo_annuncio', String(50), nullable=False),
                Column('categoria_annuncio', String(50), nullable=False),
                Column('prezzo_per_giorno_annuncio', Integer, nullable=False),
                Column('descrizione_annuncio', String(200), nullable=False),
                Column('data_inizio_noleggio', String(30), nullable=False),
                Column('data_fine_noleggio', String(30), nullable=False),
                Column('data_inserimento_annuncio', String(30), nullable=False),
                Column('id_utente_rf_annuncio', String(12), nullable=False)
                )
mapper(Annuncio, annunci)


# CLASSE PER LA GESTIONE DELLE ECCEZIONI DEGLI ANNUNCI
class AnnuncioException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


def form_add_annuncio(db, form_annuncio, id_utente):
    # save form information into session user cookie
    titolo = session["titolo_annuncio"] = form_annuncio.titolo_annuncio.data
    categoria = session["categoria_annuncio"] = form_annuncio.categoria_annuncio.data
    descrizione = session["descrizione_annuncio"] = form_annuncio.descrizione_annuncio.data
    prezzo = session["prezzo_per_giorno_annuncio"] = form_annuncio.prezzo_per_giorno_annuncio
    data_inizio = session["data_inizio_noleggio_annuncio"] = form_annuncio.data_inizio_noleggio_annuncio.data
    data_fine = session["data_fine_noleggio_annuncio"] = form_annuncio.data_fine_noleggio_annuncio.data
    data_inserimento = session["data_inserimento_annuncio"] = form_annuncio.data_inserimento_annuncio
    disponibile = session["disponibile"] = form_annuncio.disponibile
    immagine = session["immagine_annuncio"] = form_annuncio.immagine_annuncio.data

    submit_annuncio = form_annuncio.submit_annuncio

    # reset the form
    form_annuncio.titolo_annuncio.data = ""
    form_annuncio.categoria_annuncio.data = ""
    form_annuncio.descrizione_annuncio.data = ""
    form_annuncio.prezzo_per_giorno_annuncio = ""
    form_annuncio.data_inizio_noleggio_annuncio.data = ""
    form_annuncio.data_fine_noleggio_annuncio.data = ""
    form_annuncio.data_inserimento_annuncio = ""
    form_annuncio.disponibile = ""
    form_annuncio.immagine_annuncio.data = ""

    nuovo_annuncio = Annuncio(titolo, categoria, descrizione, prezzo, data_inizio, data_fine, data_inserimento,
                              disponibile, id_utente)

    return redirect(url_for("TEST_RISULTATO"))


# Metodo per aggiungere un nuovo annuncio al database
def add_annuncio(db, annuncio_inserito):
    try:
        db.connect()
        nuovo_utente = annuncio_inserito
        if nuovo_utente is None:
            raise AnnuncioException("Annuncio non valido\n")
        else:
            # Aggiunge un nuovo utente nel database
            db_session.add(annuncio_inserito)
            db_session.commit()
    except exc.SQLAlchemyError as ex:
        print(ex.__doc__)
        return ex

    return None
