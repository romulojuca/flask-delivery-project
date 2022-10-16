import wtforms
from flask_wtf import FlaskForm
from flask_wtf.file import FileField


class UserForm(FlaskForm):
    email = wtforms.StringField(
        "Email", [wtforms.validators.DataRequired(), wtforms.validators.Email()]
    )
    password = wtforms.PasswordField("Senha", [wtforms.validators.DataRequired()])
    foto = FileField("Foto")
