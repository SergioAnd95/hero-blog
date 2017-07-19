from app import db
from sqlalchemy_utils import ChoiceType, PasswordType


class User(db.Model):
    USER_ROLE = (
        ('regular_user', 1),
        ('admin', 2)
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(30), unique=True)
    role = db.Column(ChoiceType(USER_ROLE), default=1)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ))