import os
from os import walk

from flask import Blueprint, render_template, session, redirect, url_for

from project.main.forms import RegistrationFormRicerca
from project.ruoli.models import Permission
import numpy

main_blueprint = Blueprint(
    "main",
    __name__,
    template_folder="templates",
    static_folder='../static'
)

'''
Permissions may also need to be checked from templates, 
so the Permission class with all its constants needs to be accessible to them. 
To avoid having to add a template argument in every render_template() call, 
a context processor can be used. 
Context processors make variables available to all templates during rendering
'''


@main_blueprint.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


@main_blueprint.route("/", methods=['GET', 'POST'])
def index():
    form_ricerca = RegistrationFormRicerca()
    categoria_trovata = None

    if form_ricerca.validate_on_submit():
        oggetto_ricerca = form_ricerca.oggetto_ricerca.data
        categoria_ricerca = form_ricerca.categoria_ricerca.data
        provincia_ricerca = form_ricerca.provincia_annuncio.data
        data_inizio_noleggio_ricerca = form_ricerca.data_inizio_noleggio_ricerca.data
        data_fine_noleggio_ricerca = form_ricerca.data_fine_noleggio_ricerca.data

        submit_ricerca = form_ricerca.submit

        form_ricerca.oggetto_ricerca = ""
        form_ricerca.categoria_ricerca = ""
        form_ricerca.regione_ricerca = ""
        form_ricerca.data_inizio_noleggio_ricerca = ""
        form_ricerca.data_fine_noleggio_ricerca = ""

        f = list()
        percorso_categorie = 'project/categorie/templates'

        for (dirpath, dirnames, filenames) in walk(percorso_categorie):
            for file in filenames:
                f.append(str(file))

        for file in f:
            if file.__contains__(categoria_ricerca):
                categoria_trovata = file.replace('.html', '')
                print(categoria_trovata)
                break
            else:
                categoria_trovata = None

        return redirect(url_for('categorie.' + categoria_trovata))

    return render_template('index.html', form=form_ricerca, categoria_url=categoria_trovata)


# Gestione ritorno sulla home page
@main_blueprint.route('/HomePage')
def HomePage():
    return redirect(url_for('main.index'))
