from datetime import datetime
from random import random

from flask import Blueprint, render_template
from sqlalchemy import and_

from project.annunci.models import Annuncio
from project.gestione_immagini import download_image_annunci
from project.utenti.models import Utente

categorie_blueprint = Blueprint(
    "categorie",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


def gestisci_ricerca_categoria(categoria, provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = None
    print(data_inizio_noleggio)
    print(data_fine_noleggio)
    print(titolo)

    # caso con filtri titolo_annuncio,categoria_annuncio ,provincia_annuncio, data_inizio_noleggio, data_fine_noleggio
    if data_inizio_noleggio is not None and data_fine_noleggio is not None and titolo is not None:
        titolo = "%{0}%".format(titolo).lower()
        lista_annunci = Annuncio.query.filter(and_(Annuncio.titolo_annuncio.like(titolo),
                                                   Annuncio.categoria_annuncio.like(categoria),
                                                   Annuncio.provincia_annuncio.like(provincia),
                                                   Annuncio.data_inizio_noleggio == data_inizio_noleggio,
                                                   Annuncio.data_fine_noleggio == data_fine_noleggio)).all()

    # caso con filtri categoria_annuncio ,provincia_annuncio, data_inizio_noleggio, data_fine_noleggio
    elif data_inizio_noleggio is not None and data_fine_noleggio is not None and titolo is None:
        lista_annunci = Annuncio.query.filter(and_(Annuncio.categoria_annuncio.like(categoria),
                                                   Annuncio.provincia_annuncio.like(provincia),
                                                   Annuncio.data_inizio_noleggio == data_inizio_noleggio,
                                                   Annuncio.data_fine_noleggio == data_fine_noleggio)).all()


    else:
        lista_annunci = Annuncio.query.filter(and_(Annuncio.categoria_annuncio.like(categoria))).all()

    # Sezione dedicata allo scaricamento delle relative immagini degli annunci per la visualizzazione
    i = 1
    for annuncio in lista_annunci:
        # salvo le informazioni dell'utente che ha inserito l'annuncio
        annuncio.autore_caricato = Utente.query.filter_by(id=annuncio.id_utente_rf_annuncio).first()
        # Salvo le immagini nella cartella download
        download_image_annunci(annuncio, i)
        print(annuncio.immagine_caricata)
        i = i + 1
    print(lista_annunci)

    return lista_annunci


@categorie_blueprint.route('/categorie', methods=['GET', 'POST'])
def categorie():
    return render_template('categorie.html')


@categorie_blueprint.route('/categoria_altro/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_altro/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_altro/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_altro(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('altro', provincia, titolo, data_inizio_noleggio, data_fine_noleggio)
    return render_template('categoria_altro.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_auto/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_auto/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_auto/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_auto(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('auto', provincia, titolo, data_inizio_noleggio, data_fine_noleggio)
    return render_template('categoria_auto.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_console_e_videogiochi/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_console_e_videogiochi/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route(
    '/categoria_console_e_videogiochi/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
    methods=['GET', 'POST'])
def categoria_console_e_videogiochi(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('console_e_videogiochi', provincia, titolo, data_inizio_noleggio,
                                               data_fine_noleggio)
    return render_template('categoria_console_e_videogiochi.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_fotografia/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_fotografia/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_fotografia/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_fotografia(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('fotografia', provincia, titolo, data_inizio_noleggio,
                                               data_fine_noleggio)
    return render_template('categoria_fotografia.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_gioccatoli/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_gioccatoli/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_gioccatoli/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_giocattoli(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('giocattoli', provincia, titolo, data_inizio_noleggio,
                                               data_fine_noleggio)
    return render_template('categoria_gioccatoli.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_informatica/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_informatica/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_informatica/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_informatica(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('informatica', provincia, titolo, data_inizio_noleggio,
                                               data_fine_noleggio)

    return render_template('categoria_informatica.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_musica/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_musica/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_musica/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_musica(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('musica', provincia, titolo, data_inizio_noleggio, data_fine_noleggio)

    return render_template('categoria_musica.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_telefonia/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_telefonia/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_telefonia/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_telefonia(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('telefonia', provincia, titolo, data_inizio_noleggio, data_fine_noleggio)

    return render_template('categoria_telefonia.html', lista_annunci=lista_annunci)


@categorie_blueprint.route('/categoria_videomaker/', methods=['GET', 'POST'],
                           defaults={'provincia': None, 'titolo': None, 'data_inizio_noleggio': None,
                                     'data_fine_noleggio': None})
@categorie_blueprint.route('/categoria_videomaker/<provincia>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           defaults={'titolo': None}, methods=['GET', 'POST'])
@categorie_blueprint.route('/categoria_videomaker/<provincia>/<titolo>/<data_inizio_noleggio>/<data_fine_noleggio>/',
                           methods=['GET', 'POST'])
def categoria_videomaker(provincia, titolo, data_inizio_noleggio, data_fine_noleggio):
    lista_annunci = gestisci_ricerca_categoria('videomaker', provincia, titolo, data_inizio_noleggio,
                                               data_fine_noleggio)
    return render_template('categoria_videomaker.html', lista_annunci=lista_annunci)
