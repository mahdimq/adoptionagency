from flask_wtf import FlaskForm
from wtforms import StringField, TextField, RadioField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange


class PetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[
                       InputRequired(message="Name cannot be blank")])
    # species = StringField("Species", validators=[InputRequired(), AnyOf(["dog", "cat", "porcupine"])])
    species = SelectField("Species", choices=[
                          ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = TextField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(
        min=0, max=30, message="- Age has to be between 0 and 30"), Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for editting pets"""

    photo_url = TextField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    is_available = BooleanField("Available?")
