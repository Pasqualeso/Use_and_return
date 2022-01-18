from flask import Blueprint, render_template, flash, redirect, url_for, request

# Define blueprint
from flask_login import login_required, current_user

carrello_blueprint = Blueprint(
    "carrello",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


@carrello_blueprint.route('/carrello', methods=['GET', 'POST'])
def carrello():
    if current_user.is_authenticated:
        return render_template('carrello.html')
    else:
        return redirect(url_for('utenti.login'))
