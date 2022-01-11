from flask import Blueprint, render_template

# Define blueprint
from flask_login import login_required

from project.annunci.forms import RegistrationFormAnnuncio

annunci_blueprint = Blueprint(
    "annunci",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


@annunci_blueprint.route('/registrazione_annuncio', methods=['GET', 'POST'])
@login_required
def registrazione_annuncio():
    form = RegistrationFormAnnuncio()
    if form.validate_on_submit():
        print("ciao")
    return render_template('registrazione_annuncio.html', form=form)
