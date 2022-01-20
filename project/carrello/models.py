from project import db
from datetime import datetime


class Ordine(db.Model):
    id_ordine = db.Column(db.Integer, primary_key=True)
    importo_pagamento = db.Column(db.Integer, nullable=False)
    data_inserimento_ordine = db.Column(db.DateTime(), default=datetime.utcnow)
    id_utente_rf_ordine = db.Column(db.Integer, db.ForeignKey('utente.id'))


class Spedizione(db.Model):
    id_spedizione = db.Column(db.Integer, primary_key=True)
    data_spedizione = db.Column(db.DateTime(), default=datetime.utcnow)
    spesa_di_spedizione = db.Column(db.Integer, default=10)
    via_spedizione = db.Column(db.String(64), nullable=False)
    citta_spedizione = db.Column(db.String(64), nullable=False)
    provincia_spedizione = db.Column(db.String(64), nullable=False)
    cap_spedizione = db.Column(db.Integer, nullable=False)
    id_utente_rf_ordine = db.Column(db.Integer, db.ForeignKey('utente.id'))