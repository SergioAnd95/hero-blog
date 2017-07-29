from app import db

from sqlalchemy_utils import ChoiceType, PasswordType


class User(db.Model):
    USER_ROLE = (
        (1, 'regular user'),
        (2, 'admin')
    )

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    username = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(30),
        unique=True,
        nullable=False
    )
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    role = db.Column(ChoiceType(USER_ROLE), default=1)
    password = db.Column(
        PasswordType(
            schemes=[
                'pbkdf2_sha512',
                'md5_crypt'
            ],
            deprecated=['md5_crypt'],
        ),
        nullable=False
    )

    def __init__(self, username, email, password, first_name="", last_name="", role=1):
        '''
        User instance info for db session
        TODO: check first_name, last_name, role handling (these fields are not in form)
        '''
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.password = password
