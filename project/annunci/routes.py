import datetime
from flask import Blueprint, render_template, flash, redirect, url_for, request

# Define blueprint
from flask_login import login_required, current_user

from project import db, images
from project.annunci.forms import RegistrationFormAnnuncio
from project.annunci.models import Annuncio

annunci_blueprint = Blueprint(
    "annunci",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def convertToImageData(data, filename):
    # Convert binary data to proper format and write it on Hard disk
    with open(filename, 'wb') as file:
        file.write(data)


@annunci_blueprint.route('/registrazione_annuncio', methods=['GET', 'POST'])
@login_required
def registrazione_annuncio():
    form = RegistrationFormAnnuncio()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            id_utente_loggato = current_user.get_id()

            filename = images.save(form.immagine_annuncio.data)
            dirFile = 'project/static/uploads/images/' + filename
            fileBin = convertToBinaryData(dirFile)

            annuncio = Annuncio(titolo_annuncio=form.titolo_annuncio.data,
                                categoria_annuncio=form.categoria_annuncio.data,
                                immagine=fileBin,
                                prezzo_per_giorno_annuncio=form.prezzo_per_giorno_annuncio.data,
                                descrizione_annuncio=form.descrizione_annuncio.data,
                                data_inizio_noleggio=form.data_inizio_noleggio_annuncio.data,
                                data_fine_noleggio=form.data_fine_noleggio_annuncio.data,
                                citta_annuncio=form.citta_annuncio.data,
                                provincia_annuncio=form.provincia_annuncio.data,
                                via_annuncio=form.via_annuncio.data,
                                cap_annuncio=form.cap_annuncio.data)
            annuncio.id_utente_rf_annuncio = id_utente_loggato
            annuncio.data_inserimento_annuncio = datetime.datetime.utcnow()
            print(
                annuncio.titolo_annuncio + ' ' + annuncio.data_inizio_noleggio.__repr__() + ' ' + ' ' + annuncio.data_fine_noleggio.__repr__() + ' ' + annuncio.data_inserimento_annuncio.__repr__())
            db.session.add(annuncio)
            try:
                db.session.commit()
                flash('Annuncio aggiunto correttamente', 'success')
            except Exception as e:
                flash("Errore durante l'inserimento dell'annuncio")
                print(e)
                db.session.rollback()

    return render_template('registrazione_annuncio.html', form=form)
