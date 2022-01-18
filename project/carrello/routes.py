from flask import Blueprint, render_template


carrello_blueprint = Blueprint(
    "carrello",
    __name__,
    template_folder="templates",
    static_folder='../static'
)


@carrello_blueprint.route('/carrello', methods=['GET', 'POST'])
def carrello():
    return render_template('carrello.html')