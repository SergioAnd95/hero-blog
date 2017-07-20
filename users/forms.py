from wtforms_alchemy import ModelForm

from .models import User

from sqlalchemy.orm.attributes import InstrumentedAttribute

from wtforms import PasswordField
from wtforms.validators import DataRequired, EqualTo


class UserCreateForm(ModelForm):
    """
    Represent user registration form
    """
    class Meta:
        model = User
        exclude =['role', 'first_name', 'last_name']

        # auto generate placeholder from field name
        field_args = {
            field:{'render_kw':{'placeholder':field.replace('_', ' ')}}
            for field, val in User.__dict__.items()
            if isinstance(val, InstrumentedAttribute)
        }

    confirm = PasswordField(
        'confirm',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={'placeholder':'repeat password'}
    )