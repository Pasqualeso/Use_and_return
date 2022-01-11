# classe form barra di ricerca in index
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.validators import DataRequired


class RegistrationFormRicerca(FlaskForm):
    oggetto_ricerca = StringField("Cosa vuoi noleggiare?", validators=[DataRequired()])
    categoria_ricerca = SelectField(
        "Categoria",
        choices=[("musica", "Musica"), ("telefonia", "Telefonia"), ("console e videogiochi", "Console e videogiochi"),
                 ("informatica", "Informatica"),
                 ("accessori auto", "Accessori auto"), ("giocattoli", "Giocattoli"), ("fotografia", "Fotografia"),
                 ("video-maker", "Video-maker"), ("altro", "Altro")]
        , validators=[DataRequired()])
    regione_ricerca = SelectField(
        "Regione",
        choices=[("valle d'aosta", "Valle d'Aosta"), ("piemonte", "Piemonte"), ("liguria", "Liguria"),
                 ("lombardia", "Lombardia"), ("trentino-alto adige", "Trentino-Alto Adige"),
                 ("veneto", "Veneto"), ("friuli-venezia giulia", "Friuli-Venezia Giulia"),
                 ("emilia romagna", "Emilia Romagna"), ("toscana", "Toscana"), ("umbria", "Umbria"),
                 ("marche", "Marche"),
                 ("lazio", "Lazio"), ("abruzzo", "Abruzzo"), ("molise", "Molise"), ("campania", "Campania"),
                 ("puglia", "Puglia"), ("basilicata", "Basilicata"), ("calabria", "Calabria"),
                 ("sicilia", "Sicilia"), ("sardegna", "Sardegna"), ("non specificare", "Non Specificare"), ]

        , validators=[DataRequired()])
    data_inizio_noleggio_ricerca = DateField("Data di inizio noleggio", validators=[DataRequired()])
    data_fine_noleggio_ricerca = DateField("Data di fine noleggio", validators=[DataRequired()])

    submit = SubmitField("Submit")