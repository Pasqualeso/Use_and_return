from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DateField, FileField, SubmitField, BooleanField
from wtforms.validators import DataRequired


# classe form registrazione annuncio
class RegistrationFormAnnuncio(FlaskForm):
    titolo_annuncio = StringField("Inserisci il titolo della categoria", validators=[DataRequired()])
    categoria_annuncio = SelectField(
        "Inserisci la categoria",
        choices=[("musica", "Musica"), ("telefonia", "Telefonia"), ("console e videogiochi", "Console e videogiochi"),
                 ("informatica", "Informatica"),
                 ("accessori auto", "Accessori auto"), ("giocattoli", "Giocattoli"), ("fotografia", "Fotografia"),
                 ("video-maker", "Video-maker"), ("altro", "Altro")]
        , validators=[DataRequired()])

    immagine_annuncio = FileField("Inserisci un'immagine", validators=[DataRequired()])

    descrizione_annuncio = StringField("Inserisci una descrizione(Max 200 caratteri)", validators=[DataRequired()])

    prezzo_per_giorno_annuncio = IntegerField("Inserisci il prezzo al giorno per l'annuncio", validators=[DataRequired()])

    data_inizio_noleggio_annuncio = DateField("Inserisci una data di inizio noleggio", validators=[DataRequired()])
    data_fine_noleggio_annuncio = DateField("Inserisci una data di fine noleggio", validators=[DataRequired()])

    disponibile = BooleanField("Inserisci la disponibilità", validators=[DataRequired()])

    submit_annuncio = SubmitField("Submit")
