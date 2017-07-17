from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config.from_object('app.settings')

db = SQLAlchemy(app)
CSRFProtect(app)

from .views import core_pages
from users.views import user_pages

app.register_blueprint(core_pages)
app.register_blueprint(user_pages)