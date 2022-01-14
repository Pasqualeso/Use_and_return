from flask import Blueprint, render_template

from project.annunci.models import Annuncio
from project.gestione_immagini import download_image_annunci
from project.utenti.models import Utente

categorie_blueprint = Blueprint(
    "categorie",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


@categorie_blueprint.route('/categorie', methods=['GET', 'POST'])
def categorie():
    return render_template('categorie.html')


@categorie_blueprint.route('/categoria_altro', methods=['GET', 'POST'])
def categoria_altro():
    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='altro').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1

    print(lista_annunci)
    return render_template('categoria_altro.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_auto', methods=['GET', 'POST'])
def categoria_auto():
    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='accessori auto').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1

    print(lista_annunci)
    return render_template('categoria_auto.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_console&videogiochi', methods=['GET', 'POST'])
def categoria_console_e_videogiochi():
    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='console e videogiochi').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1

    print(lista_annunci)
    return render_template('categoria_console&videogiochi.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_fotografia', methods=['GET', 'POST'])
def categoria_fotografia():
    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='fotografia').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1

    print(lista_annunci)
    return render_template('categoria_fotografia.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_gioccatoli', methods=['GET', 'POST'])
def categoria_giocattoli():
    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='giocattoli').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1

    print(lista_annunci)
    return render_template('categoria_gioccatoli.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_informatica', methods=['GET', 'POST'])
def categoria_informatica():

    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='informatica').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1
    print(lista_annunci)

    return render_template('categoria_informatica.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_musica', methods=['GET', 'POST'])
def categoria_musica():

    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='musica').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1
    print(lista_annunci)

    return render_template('categoria_musica.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_telefonia', methods=['GET', 'POST'])
def categoria_telefonia():

    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='telefonia').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1
    print(lista_annunci)

    return render_template('categoria_telefonia.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_videomaker', methods=['GET', 'POST'])
def categoria_videomaker():

    lista_annunci = Annuncio.query.filter_by(categoria_annuncio='video-maker').all()
    i = 1
    for annuncio in lista_annunci:
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1
    print(lista_annunci)

    return render_template('categoria_videomaker.html', lista_annunci=lista_annunci)
