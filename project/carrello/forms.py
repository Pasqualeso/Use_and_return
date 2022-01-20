from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class OrdineForm(FlaskForm):

    id_ordine = IntegerField("Id ordine ", validators=[DataRequired])
    titolo_annuncio = StringField("titolo dell'annuncio", validators=[DataRequired(), Length(1, 64)])
    immagine_annuncio = FileField("immagine", validators=[DataRequired()])

    importo_pagamento = IntegerField("prezzo al giorno per l'annuncio",
                                     validators=[DataRequired()])

    submit_ordine = SubmitField("Conferma ordine")
