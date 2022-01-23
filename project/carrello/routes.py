from datetime import datetime

from flask import Blueprint, render_template, flash, redirect, url_for, request

# Define blueprint
from flask_login import login_required, current_user

from project.carrello.forms import OrdineForm
from project.carrello.models import Ordine

carrello_blueprint = Blueprint(
    "carrello",
    __name__,
    template_folder="templates",
    static_folder='../static'
)

'''
@carrello_blueprint.route('/carrello', defaults={'annuncio': None}, methods=['GET', 'POST'])
@carrello_blueprint.route('/carrello/<annuncio>/', methods=['GET', 'POST'])
def carrello(annuncio):
    form = OrdineForm()

    if current_user.is_authenticated:
        id_utente_loggato = current_user.get_id()

        return render_template('carrello.html', form=form, annuncio=annuncio, id_utente=id_utente_loggato)
    else:
        return redirect(url_for('utenti.login'))

'''


@carrello_blueprint.route('/carrello', defaults={'annuncio': None}, methods=['GET', 'POST'])
@carrello_blueprint.route('/carrello/<annuncio>/', methods=['GET', 'POST'])
def carrello(annuncio):
    form = OrdineForm()

    if current_user.is_authenticated:
        if annuncio is not None:
            id_utente_loggato = current_user.get_id()
            carrello_lista_ordini = Ordine.query.filter_by(id_utente_rf_ordine=id_utente_loggato)
            form.titolo_annuncio = annuncio.titolo_annuncio
            form.immagine_caricata = annuncio.immagine_caricata
            prezzo_per_giorno = annuncio.prezzo_per_giorno_annuncio
            calcola_giorni = datetime(annuncio.data_fine_noleggio - annuncio.data_inizio_noleggio).day

            nuovoOrdine = Ordine(titolo_annuncio=annuncio.titolo_annuncio, immagine=annuncio.immagine,
                                 id_utente_rf_ordine=id_utente_loggato)

            if form.validate_on_submit():
                id_utente_loggato = current_user.get_id()
                carrello_lista_ordini = Ordine.query.filter_by(id_utente_rf_ordine=id_utente_loggato)

        else:
            id_utente_loggato = current_user.get_id()
            carrello_lista_ordini = Ordine.query.filter_by(id_utente_rf_ordine=id_utente_loggato)

        return render_template('carrello.html', form=form, annuncio=annuncio, carrello=carrello_lista_ordini)
    else:
        return redirect(url_for('utenti.login'))
