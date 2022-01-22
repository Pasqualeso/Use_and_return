from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Length


class OrdineForm(FlaskForm):

    annuncio = None
    submit_ordine = SubmitField("Conferma ordine")
