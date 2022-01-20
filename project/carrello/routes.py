from flask import Blueprint, render_template, flash, redirect, url_for, request

# Define blueprint
from flask_login import login_required, current_user

from project.carrello.models import Ordine

carrello_blueprint = Blueprint(
    "carrello",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


@carrello_blueprint.route('/carrello', methods=['GET', 'POST'])
def carrello():
    if current_user.is_authenticated:
        id_utente_loggato = current_user.get_id()
        carrello_lista = Ordine.query.filter_by(id_utente_rf_ordine = id_utente_loggato)
        return render_template('carrello.html')
    else:
        return redirect(url_for('utenti.login'))
