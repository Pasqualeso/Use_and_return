from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, EqualTo, DataRequired


class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("submit")


################################################
#### SUPER ADVANCE FORMS with validators, session, url for, ...
class RegistrationFormUtente(FlaskForm):
    """Definition of the form

    Args:
        FlaskForm (object): FlaskForm default main class
    """

    nome_utente = StringField(
        "What's the name of the course", validators=[DataRequired()]
    )
    course_active = BooleanField("The course is active?")
    difficulty = RadioField(
        "Please the difficulty of the course:",
        choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")],
    )
    platform = SelectField(
        u"Pick the platform you want to do the course:",
        choices=[("zoom", "Zoom"), ("skype", "Skype"), ("teams", "Teams")],
    )
    # the u before the string is the casting to unicode
    note = TextAreaField()
    submit = SubmitField("Submit")