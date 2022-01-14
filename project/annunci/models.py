from datetime import datetime

from flask_login import current_user

from project import db


class Annuncio(db.Model):
    __tablename__ = 'annuncio'

    id_annuncio = db.Column(db.Integer, primary_key=True)
    titolo_annuncio = db.Column(db.String(64), nullable=False)
    categoria_annuncio = db.Column(db.String(64), nullable=False)
    immagine = db.Column(db.BLOB)
    disponibile = db.Column(db.Boolean,default=True ,nullable=False)
    prezzo_per_giorno_annuncio = db.Column(db.Integer, nullable=False)
    descrizione_annuncio = db.Column(db.String(150), nullable=False)

    data_inizio_noleggio = db.Column(db.DateTime, nullable=False)
    data_fine_noleggio = db.Column(db.DateTime, nullable=False)
    data_inserimento_annuncio = db.Column(db.DateTime(), default=datetime.utcnow)

    citta_annuncio = db.Column(db.String(64), nullable=False)
    provincia_annuncio = db.Column(db.String(64), nullable=False)
    via_annuncio = db.Column(db.String(120), nullable=False)
    cap_annuncio = db.Column(db.Integer, nullable=False)
    id_utente_rf_annuncio = db.Column(db.Integer, db.ForeignKey('utente.id'))

    immagine_caricata = None


    def __init__(self, **kwargs):
        super(Annuncio, self).__init__(**kwargs)



