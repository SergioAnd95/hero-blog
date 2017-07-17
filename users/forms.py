from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo


class UserCreateForm(FlaskForm):
    """
    Represent user registration form
    """
    login = StringField(
        'login',
        validators=[DataRequired()],
        render_kw={'placeholder': 'login'}
    )
    email = StringField(
        'email',
        validators=[Email()],
        render_kw={'placeholder': 'email'}
    )

    password = PasswordField(
        'password1',
        validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')],
        render_kw={'placeholder': 'password'}
    )

    confirm = PasswordField(
        'password2',
        validators=[DataRequired()],
        render_kw={'placeholder': 'repeat password'}
    )