from flask import Blueprint, render_template, session

from project.main.forms import RegistrationFormRicerca
from project.ruoli.models import Permission

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
    '''
     form_ricerca = RegistrationFormRicerca()

    if form_ricerca.validate_on_submit():
        session["oggetto_ricerca"] = form_ricerca.oggetto_ricerca
        session["categoria_ricerca"] = form_ricerca.categoria_ricerca
        session["regione_ricerca "] = form_ricerca.regione_ricerca
        session["data_inizio_noleggio_ricerca"] = form_ricerca.data_inizio_noleggio_ricerca
        session["data_fine_noleggio_ricerca"] = form_ricerca.data_fine_noleggio_ricerca

        submit_ricerca = form_ricerca.submit_ricerca

        form_ricerca.oggetto_ricerca = ""
        form_ricerca.categoria_ricerca = ""
        form_ricerca.regione_ricerca = ""
        form_ricerca.data_inizio_noleggio_ricerca = ""
        form_ricerca.data_fine_noleggio_ricerca = ""
    '''


    render_template('index.html')
